from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def create(self, phone, password = None, **extra_fields):
        if not phone:
            raise ValueError('Phone Number is required')
            user = self.model(phone = phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def superuser(self, phone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create(phone, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    phone = models.CharField(max_length=10, unique=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()
