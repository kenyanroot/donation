from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from project_managers.models import ProjectManager
from .models import Donations, Beneficiary, PickupStations
from NGO.forms import NgoProfileForm
from .forms import BeneficiaryForm, DonationsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.




class UpdateBeneficiaries(UpdateView):
    model = Beneficiary
    fields=('first_name', 'last_name', 'email', 'contact_number', 'address', 'profile_picture')
    template_name = 'beneficiaries.html'

    def get_success_url(self):
        pk = Beneficiary.objects.get(user=self.request.user).pk
        return f'beneficiary/update/{pk}'

    def get_context_data(self, **kwargs):
        context = super(UpdateBeneficiaries, self).get_context_data(**kwargs)
        context['pk'] = Beneficiary.objects.get(user=self.request.user).pk
        print(context['pk'])
        return context








@login_required
def beneficiary(request):
    if request.method == 'POST':
        form = BeneficiaryForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your profile has been updated!')
            except Exception as e:
                print()
                messages.error(request, 'error updating profile')
            return redirect('donorsprofile')
        else :
            try:
                form.save()
            except Exception as e:
                print(e)
                messages.error(request, 'error updating profile')

            return redirect('donorsprofile')
    else:

        form = BeneficiaryForm()
        context = {
            'form': form,
        }
        return render(request, 'beneficiaries.html', context)


def donations(request):
    beneficiary=Beneficiary.objects.get(user=request.user)
    pk= beneficiary.pk
    donations=Donations.objects.filter(beneficiary=beneficiary).all()
    context={
        'donations':donations,
        'pk':pk
    }

    return render(request, 'donations_ben.html', context)



def create_donation(request):
    #create a donation
    if request.method== 'POST':

        project_managers = request.POST.get('project_managers')
        amount = request.POST.get('amount')
        donation_type = request.POST.get('donation_type')
        poster = request.FILES.get('poster')
        donatio_description = request.POST.get('donatio_description')
        dropoff_address = request.POST.get('dropoff_address')
        print(poster,'llllllllllllllllllllllllllllllllllllllll')
        beneficiary=Beneficiary.objects.get(user=request.user)
        if project_managers != None:
            donation = Donations( beneficiary=beneficiary, amount=amount, donation_type=donation_type, poster=poster, donatio_description=donatio_description, dropoff_address=dropoff_address)
            donation.save()
        else:
            donation = Donations( beneficiary=beneficiary,amount=amount, donation_type=donation_type,
                                 poster=poster, donatio_description=donatio_description,
                                 dropoff_address=dropoff_address)
            donation.save()
            messages.success(request, 'Your donation has been created!')

        return redirect('create_donation')


    else:
        project_managers=ProjectManager.objects.all()
        pickup_centers=PickupStations.objects.all()
        pk=Beneficiary.objects.get(user=request.user).pk
        print(pickup_centers)

        context = {
            'project_managers': project_managers,
            'pickup_centers': pickup_centers,
            'pk':pk
        }


        return render(request, 'create_donation.html',context)



class DonationView(CreateView):
    model = Donations
    fields = ['dropoff_address', 'beneficiary', 'donation_type','donor','amount','donatio_description','project_managers','poster']
    template_name = 'create_donation.html'