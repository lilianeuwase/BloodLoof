from django.contrib.auth.backends import BaseBackend
from .models import Hospital

class AuthenticationBackend(BaseBackend):
    """
    Authentication Backend
    :To manage the authentication process of user
    """

    def hospital_authenticate(self, email=None, password=None):
        user = Hospital.objects1.get(email=email)
        if user is not None and user.check_password(password):
            if user.is_active:
                return user
            else:
                return "User is not activated"
        else:
            return None

    def get_user(self, user_id):
        try:
            return Hospital.objects1.get(pk=user_id)
        except Hospital.DoesNotExist:
            return None

