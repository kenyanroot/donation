from django.db import models
from django.conf import settings
from django.urls import reverse

from donors.models import Donors
from project_managers.models import ProjectManager

User = settings.AUTH_USER_MODEL
# Create your models here.

class NgoProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_picture = models.ImageField(upload_to='beneficiaries/profile_pictures/')
    headquarters = models.CharField(max_length=100)
    director= models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
        verbose_name_plural = 'None Governmental Organizations'

class NGOdonations(models.Model):
    beneficiary = models.ForeignKey(NgoProfile, on_delete=models.CASCADE, blank=True, null=True)
    donor = models.ForeignKey(Donors, on_delete=models.CASCADE, blank=True, null=True)
    project_managers = models.ForeignKey(ProjectManager, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(null=True, blank=True)
    donation_type = models.CharField(max_length=100, null=True, blank=True)
    poster = models.ImageField(upload_to='beneficiaries/poster/', null=True, blank=True)
    donatio_description = models.CharField(null=True, blank=True, max_length=200)
    delivered = models.BooleanField(default=False)
    delivered_date = models.DateTimeField(null=True, blank=True)
    delivery_failed = models.BooleanField(default=False)
    delivery_failed_reason = models.CharField(max_length=100,blank=True)
    dropoff_address = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    accepted= models.BooleanField(default=False)
    progress_report=models.ForeignKey('NGO.ProgressReports',on_delete=models.CASCADE,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('beneficiaries:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.beneficiary.first_name + ' ' + self.beneficiary.last_name

    class Meta:
        verbose_name_plural = 'Donations'


class ProgressReports(models.Model):
    project=models.ForeignKey(NGOdonations, on_delete=models.CASCADE)
    project_manager=models.ForeignKey(ProjectManager, on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=100)
    file=models.FileField(upload_to='beneficiaries/progress_report/')