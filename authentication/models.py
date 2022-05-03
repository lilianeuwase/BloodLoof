# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, UserManager

# #Create your models here.
# class Donor(AbstractBaseUser):
#     username = models.CharField(('username'), unique=True, null = True, max_length = 100)
#     fname = models.CharField(('first name'), max_length=30, blank=True)
#     lname = models.CharField(('last name'), max_length=30, blank=True)
#     email = models.EmailField(('email address'), unique=True)
#     password = models.CharField(('password'), max_length=30, blank=True)
#     phone_number = models.CharField(('phone number'), max_length=14, blank=True)
    
    
#     is_donor = models.BooleanField(default=False, null = False)
#     is_staff = models.BooleanField(default=False, null = False)
#     house_address = models.TextField(max_length= 200, null = False)
#     objects = UserManager()
#     USERNAME_FIELD = "username"
    
    


    