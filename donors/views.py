from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from beneficiaries.models import Donations, PickupStations
from  .forms import DonorForm
# Create your views here.
from .models import Donors

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
    donations_list = Donations.objects.filter(donor=donor).all()
    paginator = Paginator(donations_list, 8)
    page = request.GET.get('page')
    donations = paginator.get_page(page)
    return render(request, 'donations.html', {'donations': donations})

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
        context={
            'donation':Donations.objects.filter(pk=pk).get(),
            'pickups':pickups,
        }
        return render(request, 'donate.html',context)
