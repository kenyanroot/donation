from django.urls import path,include
from .views import donations,donate,DonorView,save_order
urlpatterns = [
    # path('donors/first', donorsprofile, name='donorsprofile'),
    path('donations', donations, name='donations'),
    path('donate/<int:pk>', donate, name='donate'),
    path('donor/<int:pk>', DonorView.as_view(), name='donor'),
    path('save_order/<int:pk>', save_order, name='save_order'),
]