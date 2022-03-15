from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from beneficiaries.models import Beneficiary
from donors.models import Donors
from NGO.models import NgoProfile
from project_managers.models import ProjectManager
User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_beneficiary:
            beneficiary=Beneficiary.objects.create(user=instance)
            beneficiary.save()





@receiver(post_save, sender=User)
def update_pm_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_project_manager:
            print('kkkkkkkkkkkkk', instance, 'ooooooooooooooooooooo')

            pm=ProjectManager.objects.create(user=instance)
            pm.save()


@receiver(post_save, sender=User)
def update_donor_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_donor:
            donor=Donors.objects.create(user=instance)
            donor.save()


@receiver(post_save, sender=User)
def update_ngo_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_ngo:
            profile=NgoProfile.objects.create(user=instance)
            profile.save()







@receiver(post_save, sender=User)
def update_admin_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_admin:
            print('user is admin')

            pass
#
#
# @receiver(post_save, sender=User)
# def save_beneficiary_profile(sender, instance, **kwargs):
#     if instance.is_beneficiary:
#         instance.beneficiary.save()
#         instance.refresh_from_db()
#
#
#     else:
#         pass


#
# @receiver(post_save, sender=User)
# def save_ngo_facility(sender, instance, **kwargs):
#     if instance.is_ngo:
#         print('kkkkkkkkkkkkk', instance)
#         instance.ngoprofile.save()
#
#         instance.refresh_from_db()
#     else:
#         pass


@receiver(post_save, sender=User)
def save_donor_profile(sender, instance, **kwargs):
    if instance.is_donor:
        print('donor')
        # instance.donors.save()
        instance.refresh_from_db()
    else:
        pass

#
# @receiver(post_save, sender=User)
# def save_pm_profile(sender, instance, **kwargs):
#     if instance.is_project_manager:
#         print('kkkkkkkkkkkkkkkkkkkkkppppppppkkk')
#         instance.projectmanager.save()
#         instance.refresh_from_db()
#     else:
#         pass

#
# @receiver(post_save, sender=User)
# def save_docnor_profile(sender, instance, **kwargs):
#     if instance.is_donor:
#         print('kkkkkkkkkkkkkkkdonooorkkkkkkppppppppkkk')
#         instance.donor.save()
#         instance.refresh_from_db()
#     else:
#         pass