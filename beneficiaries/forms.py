from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from authentication.models import MyUser
from beneficiaries.models import Beneficiary, Donations


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    # def init_(self, *args, **kwargs):
    #     super(SignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['username'].widget.attrs['placeholder'] = 'Username'
    #     self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    #     self.fields['password1'].help_text = '<span class="form-text text-muted"><small>Your password can\'t be too similar to your other personal information. Your password must contain at least 8 characters. Your password can\'t be a commonly used password. Your password can\'t be entirely numeric.</small></span>'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Confirm password'
    #     self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    #     self.fields['first_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
    #     self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    #     self.fields['last_name'].widget.attrs['class'] = 'form-control'
    #     self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
    #     self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['placeholder'] = 'Email'
    #

class BeneficiaryForm(forms.ModelForm):
    class Meta:
        model = Beneficiary
        fields = ('first_name', 'last_name', 'email', 'contact_number', 'address', 'profile_picture')
    #
    # def __init__(self):
    #     super(BeneficiaryForm, self).__init__()
    #     self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['contact_number'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['address'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['profile_picture'].widget.attrs.update({'class': 'form-control'})


class DonationsForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = ('dropoff_address', 'beneficiary', 'donation_type','donor','amount','donatio_description','project_managers','poster')
        # class Meta:



        # beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
        # donor = models.ForeignKey(Donors, on_delete=models.CASCADE, blank=True, null=True)
        # project_managers = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, blank=True, null=True)
        # amount = models.IntegerField()
        # donation_type = models.CharField(max_length=100, null=True, blank=True)
        # donatio_description = models.CharField(null=True, blank=True, max_length=200)
        # delivered = models.BooleanField(default=False)
        # delivered_date = models.DateTimeField(null=True, blank=True)
        # delivery_failed = models.BooleanField(default=False)
        # delivery_failed_reason = models.CharField(max_length=100)
        # dropoff_address = models.CharField(max_length=200)
        # date_added = models.DateTimeField(auto_now_add=True)