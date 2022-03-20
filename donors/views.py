from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from beneficiaries.models import Donations, PickupStations
from .forms import DonorForm
# Create your views here.
from .models import Donors


class DonorView(UpdateView):
    model = Donors
    fields = ('first_name', 'last_name', 'email', 'contact_number', 'address', 'profile_picture')

    template_name = 'user-profile.html'

    def get_success_url(self):
        pk = Donors.objects.get(user=self.request.user).pk
        return f'/donor/{pk}'

    def get_context_data(self, **kwargs):
        context = super(DonorView, self).get_context_data(**kwargs)
        context['pk'] = Donors.objects.get(user=self.request.user).pk
        print(context['pk'])
        return context


@login_required(login_url='/login/redirect')
def donorsprofile(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('donorsprofile')
    else:
        form = DonorForm()

    return render(request, 'user-profile.html', {'form': form})


@login_required(login_url='/login/redirect')
def donations(request):
    donor = Donors.objects.filter(user=request.user).get()
    pk = Donors.objects.filter(user=request.user).get().pk
    donations_list = Donations.objects.filter(donor=donor).all()
    paginator = Paginator(donations_list, 8)
    page = request.GET.get('page')
    donations = paginator.get_page(page)
    return render(request, 'donations.html', {'donations': donations, 'pk': pk, })


@login_required(login_url='/login/redirect')
def donate(request, pk):
    if request.method == 'POST':
        donation = Donations.objects.filter(id=pk).get()
        description = request.POST['description']
        dropoff_address = request.POST['pickupCenter']
        try:
            donor = Donors.objects.filter(user=request.user).get()
            print('lllllllllllllllllllllllllllll',donor)

        except Donors.DoesNotExist:
            donor = Donors.objects.create(user=request.user)
            print('lllllllllllllllllllllllllllll',donor)
            messages.error(request, 'Please create a donor account to donate')
            return redirect('signup_donor')
        donation.donor = donor
        donation.donatio_description = description
        donation.dropoff_address = dropoff_address
        donation.save()
        messages.success(request, 'You have donated successfully!')
        current_site = get_current_site(request)

        subject = 'Donation Made'
        message = f'Thank you for your contribution. The donation can be dropped off at {dropoff_address} Pickup center and we will ensure it gets to the right hands'
        send_mail(

            subject,
            message,
            settings.EMAIL_HOST_USER,
            [donor.email],
            fail_silently=settings.FAIL_SILENTLY,

        )

        subject = 'Donation Recieved'
        message = f'Hi {donation.beneficiary.first_name}, A donation has been made.Please be patient as we await its reception. We will notify you when it Arrives'
        send_mail(

            subject,
            message,
            settings.EMAIL_HOST_USER,
            [donation.beneficiary.email],
            fail_silently=settings.FAIL_SILENTLY,

        )

        return redirect('donations')

    else:
        pkay=pk
        pickups = PickupStations.objects.all()
        try:
            pk = Donors.objects.filter(user=request.user).get().pk
            context = {
                'donation': Donations.objects.filter(pk=pkay).get(),
                'pickups': pickups,
                'pk': pk,
            }
            return render(request, 'donate.html', context)
        except Exception as e:
            print(e)
            messages.error(request, 'Please create a donor account to donate')
            return redirect('signup_donor')



def save_order(request,pk):
    if request.method == 'POST':
        recipient=Donations.objects.filter(pk=pk).get()
        email=recipient.beneficiary.email
        subject = 'Donation Recieved'
        message = f'Hi {recipient.beneficiary.first_name}, A donation has been made.We will process the funds within 48 hours so you can receive them.Thank you'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=settings.FAIL_SILENTLY,

        )
        email=recipient.donor.email
        subject = 'Donation Recieved'
        message = f'Hi {recipient.donor.first_name}, Thank you for your support.Your donation has been received .'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
        )



        return HttpResponse('Thank you for your support.Your donation has been received .')
    else:
        return HttpResponse('Not allowed')
