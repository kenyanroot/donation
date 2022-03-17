from django.urls import path,include
from .views import pmpage,UpdatePm,Projects,accept_project,reject_project,upload_prgress_reports,projects_list

urlpatterns = [
    path('projectManager', pmpage, name='pmpage'),
    path('updatePm/<int:pk>', UpdatePm.as_view(), name='updatePm'),
    path('pm/projects', Projects.as_view(), name='projects'),
    path('pm/accept_project/<int:pk>', accept_project, name='accept_project'),
    path('pm/reject_project/<int:pk>', reject_project, name='reject_project'),
    path('pm/upload_progress_reports/<int:pk>', upload_prgress_reports, name='upload_progress_reports'),
    path('pm/projects_list', projects_list, name='projects_list'),

    ]