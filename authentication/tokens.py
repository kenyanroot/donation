from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

from NGO.models import NgoProfile
from donors.models import Donors
from project_managers.models import ProjectManager
from beneficiaries.models import Beneficiary
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        if user.is_donor:
            donor = Donors.objects.filter(user=user).get()
            return (


                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(donor.email_confirmed)
            )
        elif user.is_beneficiary:
            beneficiary=Beneficiary.objects.filter(user=user).get()
            return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(beneficiary.email_confirmed)

            )
        elif user.is_ngo:
            ngos = NgoProfile.objects.filter(user=user).get()
            return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(ngos.email_confirmed)
            )
        elif user.is_project_manager:
            pm=ProjectManager.objects.filter(user=user).get()
            return (
                six.text_type(user.pk) + six.text_type(timestamp) +
                six.text_type(pm.email_confirmed)
            )
        else:
            pass


account_activation_token = AccountActivationTokenGenerator()