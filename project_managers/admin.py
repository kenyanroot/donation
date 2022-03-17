from django.contrib import admin
from .models import ProjectManager
# Register your models here.


class ProjectmanagerAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name')


admin.site.register(ProjectManager,ProjectmanagerAdmin)