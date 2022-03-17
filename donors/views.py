from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from beneficiaries.models import Donations, PickupStations
from  .forms import DonorForm
# Create your views here.
from .models import Donors


class DonorView(UpdateView):
    model = Donors
    fields = ('first_name', 'last_name', 'email', 'contact_number', 'address','profile_picture')

    template_name = 'user-profile.html'

    def get_success_url(self):
        pk = Donors.objects.get(user=self.request.user).pk
        return f'/donor/{pk}'
    def get_context_data(self, **kwargs):
        context = super(DonorView, self).get_context_data(**kwargs)
        context['pk'] = Donors.objects.get(user=self.request.user).pk
        print(context['pk'])
        return context


@login_required
def donorsprofile(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('donorsprofile')
    else:
        form = DonorForm()

    return render(request, 'user-profile.html',{'form': form})

@login_required
def donations(request):
    donor=Donors.objects.filter(user=request.user).get()
    pk=Donors.objects.filter(user=request.user).get().pk
    donations_list = Donations.objects.filter(donor=donor).all()
    paginator = Paginator(donations_list, 8)
    page = request.GET.get('page')
    donations = paginator.get_page(page)
    return render(request, 'donations.html', {'donations': donations,'pk':pk,})

@login_required
def donate(request,pk):
    if request.method == 'POST':
        donation = Donations.objects.filter(id=pk).get()
        description=request.POST['description']
        dropoff_address=request.POST['pickupCenter']

        donor=Donors.objects.filter(user=request.user).get()
        donation.donor=donor
        donation.donatio_description=description
        donation.dropoff_address=dropoff_address
        donation.save()
        messages.success(request, 'You have donated successfully!')
        current_site = get_current_site(request)

        subject = 'Donation Made'
        message = f'Thank you for your contribution. The donation can be dropped off at {dropoff_address} Pickup center and we will ensure it gets to the right hands'
        send_mail(

            subject,
            message,
            'djangoapis20213@gmail.com',
            [donor.email],
            fail_silently=False,

        )

        subject='Donation REcieved'
        message=f'Hi {donation.beneficiary.first_name}, A donation has been made.Please be patient as we await its reception. We will notify you when it Arrives'
        send_mail(

            subject,
            message,
            'djangoapis20213@gmail.com',
            [donation.beneficiary.email],
            fail_silently=False,

        )


        return redirect('donations')

    else:
        pickups=PickupStations.objects.all()
        pk=Donors.objects.filter(user=request.user).get().pk
        context={
            'donation':Donations.objects.filter(pk=pk).get(),
            'pickups':pickups,
            'pk':pk,
        }
        return render(request, 'donate.html',context)
