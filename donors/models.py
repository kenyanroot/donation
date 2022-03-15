from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()
# Create your models here.

class Donors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)#to remove blank on new db
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_picture = models.ImageField(upload_to='beneficiaries/profile_pictures/')
    date_added = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name_plural = 'Donors'

