from django.contrib import admin

# Register your models here.
from .models import NgoProfile

class NgoProfileAdmin(admin.ModelAdmin):
    list_display = ('name','email')


admin.site.register(NgoProfile,NgoProfileAdmin)