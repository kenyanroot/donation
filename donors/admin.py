from django.contrib import admin
from .models import Donors
# Register your models here.



class DonorAdmin(admin.ModelAdmin):
    list_display = ('email','first_name')

admin.site.register(Donors,DonorAdmin)