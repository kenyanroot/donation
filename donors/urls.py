from django.urls import path,include
from .views import donorsprofile,donations,donate
urlpatterns = [
    path('donors', donorsprofile, name='donorsprofile'),
    path('donations', donations, name='donations'),
    path('donate/<int:pk>', donate, name='donate'),
]