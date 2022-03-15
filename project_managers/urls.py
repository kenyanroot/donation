from django.urls import path,include
from .views import pmpage

urlpatterns = [
    path('projectManager', pmpage, name='pmpage'),

    ]