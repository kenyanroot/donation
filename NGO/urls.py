from django.urls import path

from .views import ngoprofile, ngo_donations, create_donation, UpdateNgo

urlpatterns = [
    path('ngo', ngoprofile, name='ngoprofile'),
    path('ngo/donations', ngo_donations, name='ngo_donations'),
    path('ngo/donations/create', create_donation, name='create_donation_ngo'),
    path('ngo/update/<int:pk>', UpdateNgo.as_view(), name='ngoprofile_update'),

]
