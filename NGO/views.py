from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from beneficiaries.models import PickupStations
from project_managers.models import ProjectManager
from .forms import NgoProfileForm
# Create your views here.
from .models import NgoProfile, NGOdonations


@login_required
def ngoprofile(request):
    if request.method == 'POST':
        form = NgoProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('ngoprofile')
        else:
            messages.error(request, 'profile update failed!')
            return redirect('ngoprofile')

    else:

        form = NgoProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'ngo.html', context)

@login_required()
def ngo_donations(request):
    beneficiary = NgoProfile.objects.get(user=request.user)
    donations = NGOdonations.objects.filter(beneficiary=beneficiary).all()

    context = {
        'donations': donations,
    }

    return render(request, 'ngo_donations_list.html', context)


def create_donation(request):
    # create a donation
    if request.method == 'POST':

        project_managers = request.POST.get('project_managers')
        amount = request.POST.get('amount')
        donation_type = request.POST.get('donation_type')
        poster = request.FILES.get('poster')
        donatio_description = request.POST.get('donatio_description')
        dropoff_address = request.POST.get('dropoff_address')
        print(project_managers)
        beneficiary = NgoProfile.objects.get(user=request.user)
        if project_managers != None:
            donation = NGOdonations(beneficiary=beneficiary, project_managers=project_managers, amount=amount,
                                    donation_type=donation_type, poster=poster, donatio_description=donatio_description,
                                    dropoff_address=dropoff_address)
            donation.save()
        else:
            donation = NGOdonations(beneficiary=beneficiary, amount=amount, donation_type=donation_type,
                                    poster=poster, donatio_description=donatio_description,
                                    dropoff_address=dropoff_address)
            donation.save()
            messages.success(request, 'Your donation has been created!')

        return redirect('create_donation_ngo')


    else:
        project_managers = ProjectManager.objects.all()
        pickup_centers = PickupStations.objects.all()
        print(pickup_centers)

        context = {
            'project_managers': project_managers,
            'pickup_centers': pickup_centers,
        }

        return render(request, 'create_donation.html', context)
