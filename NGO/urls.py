from django.urls import path,include
from .views import ngoprofile,ngo_donations,create_donation
urlpatterns = [
    path('ngo', ngoprofile, name='ngoprofile'),
    path('ngo/donations',ngo_donations,name='ngo_donations'),
path('ngo/donations/create',create_donation,name='create_donation_ngo')

    ]