# from django.contrib.auth.base_user import BaseUserManager
# from django.utils import timezone


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def _create_user(self, username, email, password, hospital_name, **extra_fields):
#         if not email:
#             raise ValueError('The given email must be set')
    
#         email = self.normalize_email(email) #New
#         user = self.model(username = username, email = email, password=password, hospital_name = hospital_name, **extra_fields)
#         user.set_password(password)#New
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, email, password=None, hospital_name=None, **extra_fields):
#         return self._create_user(username, email, password, hospital_name, **extra_fields)

#     def create_superuser(self, username, email, password, **extra_fields):
#         return self._create_user(username, email, password, True, True,
#                                  **extra_fields)