from django.contrib import admin

# Register your models here.
from .models import NgoProfile,NGOdonations,ProgressReports

class NgoProfileAdmin(admin.ModelAdmin):
    list_display = ('name','email')


admin.site.register(NgoProfile,NgoProfileAdmin)


#register NGOdonations to admin
class NGOdonationsAdmin(admin.ModelAdmin):
    list_display = ('donatio_description','donor','project_managers','donation_type')


admin.site.register(NGOdonations,NGOdonationsAdmin)


class ProgressReportsAdmin(admin.ModelAdmin):
    list_display = ('name','file')
    #many to many field



admin.site.register(ProgressReports,ProgressReportsAdmin)
