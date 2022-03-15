from django.urls import path,include
from .views import index,CausesList
urlpatterns = [
    path('', index, name='home'),
    path('causes/', CausesList.as_view(), name='causes'),

    ]