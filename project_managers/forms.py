from django import forms
from .models import ProjectManager

#form for updating PM profile
class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model = ProjectManager
        fields = ('first_name', 'last_name', 'email', 'contact_number', 'address', 'profile_picture')

    # def __init__(self):
    #     super(ProjectManagerForm, self).__init__()
    #     self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['address'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})
