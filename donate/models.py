from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django.contrib.auth.models import User

import uuid


# Create your models here.
class Donor(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=14, null=True)
    dob = models.DateField(max_length=12, null=True)
    weight = models.CharField(max_length=6, null=True)
    height = models.CharField(max_length=4, null=True)
    available_time = models.DateTimeField(null=True)
    hospital = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    donated = models.BooleanField(null = True)
    
    
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['dob', 'weight', 'height' , 'available_time',  'hospital', 'username']
    
    objects = UserManager()