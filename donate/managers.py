from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, dob, **extra_fields):
        if not phone_number:
            raise ValueError('The given phone number must be set')
    
        user = self.model(phone_number = phone_number, dob = dob, **extra_fields)
        
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, dob=None, **extra_fields):
        return self._create_user(phone_number, dob, **extra_fields)

    # def create_superuser(self, username, email, password, **extra_fields):
    #     return self._create_user(username, email, password, True, True,
    #                              **extra_fields)

