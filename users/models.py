from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):

    def create_superuser(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have password")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user




class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


