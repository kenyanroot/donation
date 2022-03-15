from django.conf import settings
from django.db import models
from django.urls import reverse

from donors.models import Donors
from project_managers.models import ProjectManager

User = settings.AUTH_USER_MODEL
# Create your models here.


class Beneficiary(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_picture= models.ImageField(upload_to='beneficiaries/profile_pictures/')
    date_added = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name_plural = 'Beneficiaries'


class Donations(models.Model):
    beneficiary=models.ForeignKey(Beneficiary, on_delete=models.CASCADE)
    donor=models.ForeignKey(Donors, on_delete=models.CASCADE,blank=True, null=True)
    project_managers=models.ForeignKey(ProjectManager, on_delete=models.CASCADE,blank=True, null=True)
    amount=models.IntegerField( null=True,blank=True)
    donation_type=models.CharField(max_length=100,null=True, blank=True)
    poster=models.ImageField(upload_to='beneficiaries/poster/',null=True, blank=True)
    donatio_description=models.CharField(null=True, blank=True,max_length=200)
    delivered=models.BooleanField(default=False)
    delivered_date=models.DateTimeField(null=True, blank=True)
    delivery_failed=models.BooleanField(default=False)
    delivery_failed_reason=models.CharField(max_length=100)
    dropoff_address=models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('beneficiaries:detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.donation_type
    class Meta:
        verbose_name_plural = 'Donations'

class PickupStations(models.Model):
    doations=models.ForeignKey(Donations, on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    contact_number=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    building=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Pickup Stations'