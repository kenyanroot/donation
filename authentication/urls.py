from django.urls import path,include
from .views import login_view,logout_view,activate,account_activation_sent,signup_donor,signup_ngo,signup_beneficiary,signup_pm,profile_view
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    path('signup/donor/', signup_donor, name='signup_donor'),
    path('signup/ngo/', signup_ngo, name='signup_ngo'),
    path('signup/beneficiary/', signup_beneficiary, name='signup_beneficiary'),
    path('signup/pm/', signup_pm, name='signup_pm'),
    path('profile', profile_view, name='profile_redirect'),


    ]