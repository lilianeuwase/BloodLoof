from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

import uuid


# Create your models here.
class Donor(AbstractBaseUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=14, null=True)
    phone_number = models.CharField(max_length=14, null=True)
    dob = models.DateField(max_length=14, null=True)
    weight = models.DecimalField(null=True, max_digits=5, decimal_places=5)
    height = models.DecimalField(max_digits=5, decimal_places=5, null=True)
    available_time = models.DateTimeField(null=True)
    address = models.CharField(max_length=200, null=True)
    hospital = models.CharField(max_length=14, null=True)
    
    
    USERNAME_FIELD = "phone_number"
    
    objects = UserManager()