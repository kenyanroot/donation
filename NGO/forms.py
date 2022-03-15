from django import forms
from .models import NgoProfile

#form for NGO profile update
class NgoProfileForm(forms.ModelForm):
    class Meta:
        model = NgoProfile
        fields =  ('name', 'headquarters', 'director','email', 'contact_number', 'address','profile_picture')

    # def __init__(self, *args, **kwargs):
    #     super(NgoProfileForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['headquarters'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['director'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['address'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})
