from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import ProjectManagerForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
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