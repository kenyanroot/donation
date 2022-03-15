from django.contrib import admin
from .models import Beneficiary, Donations,PickupStations
# Register your models here.

#register beneficiary to Admin
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name',)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Donations)
admin.site.register(PickupStations)
