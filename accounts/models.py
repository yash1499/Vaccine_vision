from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from django_countries.fields import CountryField
from treebeard.mp_tree import MP_Node


class BaseProfile(AbstractBaseUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    date_of_birth = models.DateField(null=True)

    age = models.FloatField(null=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(null=True,max_length=150)

    pincode = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = CountryField(null=True)
    address = models.CharField(null=True,max_length=500)
    is_patient = models.NullBooleanField(default=True)
    is_doctor = models.NullBooleanField(default=False)
    gender = models.CharField(choices = GENDER,default= 'male',max_length=100,null=True)

    # objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return "{} {}".format(self.first_name,self.last_name)


class Patient(BaseProfile,MP_Node):
    path = models.CharField(max_length=255, unique=True, null=True, default='')
    depth = models.PositiveIntegerField(null=True, default=0)
    profession = models.CharField(max_length=100,null=True)
    last_visit = models.DateField(null=True)				# last visit to the doctor : or taken any vaccination

    class Meta:
        db_table = 'patient'

    def last_checked(self):
        return self.last_visit


class Doctor(BaseProfile):

    rating = models.IntegerField(null=True)				# rating out of 5
    experience = models.IntegerField(null=True)

    class Meta:
        db_table = 'doctor'