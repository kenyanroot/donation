from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import UpdateView, ListView

from NGO.models import NgoProfile, NGOdonations, ProgressReports
from .forms import ProjectManagerForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .models import ProjectManager


@login_required
def pmpage(request):
    if request.method=='POST':
        form = ProjectManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('pmpage')
        else:
            messages.success(request, 'error updating profile')
    else:

        form = ProjectManagerForm()
        context = {
            'form': form,
        }

        return render(request, 'project_managers.html',context)


class UpdatePm(UpdateView):
    model = ProjectManager
    fields = ['first_name', 'last_name', 'email', 'contact_number', 'address', 'profile_picture']
    template_name = 'project_managers.html'
    def get_success_url(self):
        pk=self.kwargs['pk']
        return f'/updatePm/{pk}'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pk'] = ProjectManager.objects.get(user=self.request.user).pk
        print(context['pk'])
        return context



def  projects_list(request):
    projects = NGOdonations.objects.filter(project_managers=ProjectManager.objects.get(user=request.user))
    # reports =  NGOdonations.objects.filter(project_managers=ProjectManager.objects.get(user=request.user)).get().donatio_description#ProgressReports.objects.filter(project_manager=ProjectManager.objects.get(user=request.user)).all()
    # print(reports)
    pk=ProjectManager.objects.get(user=request.user).pk
    context = {
        'object_list': projects,
        'pk':pk
    }
    return render(request, 'projects.html', context)


class Projects(ListView):
    model = NgoProfile
    template_name = 'projects.html'
    context_object_name = 'projects'
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = ProjectManager.objects.get(user=self.request.user).pk
        pk = context['pk']
        #
        # project_manager= P.objects.get(user=self.request.user).progress_reports.all()
        #
        #
        # print(project_manager)


        return context


def accept_project(request, pk):
    project = NGOdonations.objects.get(pk=pk)
    project.accepted = True

    project.save()
    project = NGOdonations.objects.get(pk=pk)
    print(project.accepted,'lllllll')
    return redirect('projects_list')

def reject_project(request, pk):
    project = NGOdonations.objects.get(pk=pk)
    project.accepted = False
    project.save()
    return redirect('projects_list')


def upload_prgress_reports(request, pk):
    project = NGOdonations.objects.filter(pk=pk).get()
    if request.method == 'POST':
        progress_report = request.FILES['progress_report']
        name=request.POST['name']
        pm=ProjectManager.objects.get(user=request.user)
        print(pm)
        report=ProgressReports.objects.create(name=name,file=progress_report,project_manager=pm,project=project)
        report.save()
        project.progress_report=report
        project.save()
        # project.progress_report=report
        # project.save()
        messages.success(request, 'Your progress report has been uploaded!')

            #send email to stakeholders of the project telling the progress report has been uploaded
        subject = 'Progress report uploaded'
        message =  'A progress report to a project in which you are a stakeholder has been uploaded.Please log in to your aacount to view it'



        if project.donor:
            send_mail(

                subject,
                message,
                settings.EMAIL_HOST_USER,
                [str(project.donor.email)],
                fail_silently=settings.FAIL_SILENTLY,

            )

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [str(project.beneficiary.email),],
            fail_silently=settings.FAIL_SILENTLY,

        )
        return redirect('projects_list')
    else:
        return redirect('projects_list')