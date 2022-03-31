from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from beneficiaries.models import PickupStations
from project_managers.models import ProjectManager
from .forms import NgoProfileForm
# Create your views here.
from .models import NgoProfile, NGOdonations


class UpdateNgo(UpdateView):
    model = NgoProfile
    template_name = 'ngo.html'
    fields = ('name', 'contact_number', 'email', 'headquarters', 'director', 'address', 'profile_picture')

    def get_success_url(self):
        pk = NgoProfile.objects.get(user=self.request.user).pk
        return f'/ngo/update/{pk}'

    def get_context_data(self, **kwargs):
        context = super(UpdateNgo, self).get_context_data(**kwargs)
        context['ngo'] = NgoProfile.objects.get(user=self.request.user)
        return context


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
    ngo = NgoProfile.objects.get(user=request.user)

    context = {
        'donations': donations,
        'ngo': ngo
    }

    return render(request, 'ngo_donations_list.html', context)

@login_required()
def create_donation(request):
    # create a donation
    if request.method == 'POST':

        project_managers = request.POST.get('project_managers')
        amount = request.POST.get('amount')
        donation_type = request.POST.get('donation_type')
        poster = request.FILES.get('poster')
        donatio_description = request.POST.get('donatio_description')
        dropoff_address = request.POST.get('dropoff_address')
        print(project_managers,'ppppppppppppppppppppppppmmmmmm')
        beneficiary = NgoProfile.objects.get(user=request.user)
        if project_managers == 'Select PM':
            donation = NGOdonations(beneficiary=beneficiary, amount=amount,
                                    donation_type=donation_type, poster=poster, donatio_description=donatio_description,
                                    dropoff_address=dropoff_address)
            donation.save()

            messages.success(request, 'Your donation has been created!')
        else:
            pm = ProjectManager.objects.filter(pk=project_managers).get()
            donation = NGOdonations(beneficiary=beneficiary, project_managers=pm, amount=amount,
                                    donation_type=donation_type,
                                    poster=poster, donatio_description=donatio_description,
                                    dropoff_address=dropoff_address)
            donation.save()
            print(poster)
            messages.success(request, 'Your donation has been created!')

            pm = ProjectManager.objects.filter(pk=project_managers).get()
            subject = 'New Donation'
            email = pm.email
            message = f"You have bee assigned a new donation from {beneficiary.name}! Please check your dashboard for more details."
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=settings.FAIL_SILENTLY,

            )

        return redirect('create_donation_ngo')


    else:
        project_managers = ProjectManager.objects.all()
        pickup_centers = PickupStations.objects.all()
        ngo = NgoProfile.objects.get(user=request.user)
        print(pickup_centers)

        context = {
            'project_managers': project_managers,
            'pickup_centers': pickup_centers,
            'ngo': ngo
        }

        return render(request, 'create_donation_ngo.html', context)
