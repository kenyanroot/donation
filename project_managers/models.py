from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class ProjectManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    profile_picture = models.ImageField(upload_to='beneficiaries/profile_pictures/')
    date_added = models.DateTimeField(auto_now_add=True)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    class Meta:
        verbose_name_plural = 'Project Managers'
