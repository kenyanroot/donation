from django.db import models

# Create your models here.


from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, is_donor, is_project_manager, is_beneficiary,is_ngo, password):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),

            is_donor=is_donor,
            is_project_manager=is_project_manager,
            is_beneficiary=is_beneficiary,
            is_ngo=is_ngo,
        )
        print('------------kk---', password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, is_donor=False, is_ngo=False,is_project_manager=False, is_beneficiary=False, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_donor=is_donor,
            is_project_manager=is_project_manager,
            is_beneficiary=is_beneficiary,
            is_ngo=is_ngo,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_donor = models.BooleanField(default=False)
    is_project_manager = models.BooleanField(default=False)
    is_health_facility = models.BooleanField(default=False)
    is_beneficiary = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_ngo = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

