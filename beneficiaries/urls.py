from django.urls import path,include
from .views import beneficiary,donations,create_donation,DonationView

urlpatterns = [
    path('beneficiary', beneficiary, name='beneficiary'),
    path('beneficiary/donations', donations, name='ben_donations'),
    path('beneficiary/donations/create', create_donation, name='create_donation'),
    path('beneficiary/donations/', DonationView.as_view(), name='donation_detail'),

    ]