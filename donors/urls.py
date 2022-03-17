from django.urls import path,include
from .views import donorsprofile,donations,donate,DonorView
urlpatterns = [
    path('donors', donorsprofile, name='donorsprofile'),
    path('donations', donations, name='donations'),
    path('donate/<int:pk>', donate, name='donate'),
    path('donor/<int:pk>', DonorView.as_view(), name='donor'),
]