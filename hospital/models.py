import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from django import forms


# Create your models here.
class Hospital(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null = True)
    email = models.CharField(max_length=100, null = True, unique = True)
    password = models.CharField(('password'), null=True, max_length=128, help_text=("Use  '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
    hospital_name = models.CharField(max_length=40, null=True)
    address = models.CharField(max_length=200, null=True)
    objects = UserManager()
    
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ['email', 'password', 'hospital_name']