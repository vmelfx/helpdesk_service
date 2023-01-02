from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone


class User(AbstractBaseUser):
    id = models.BigAutoField()
    password = AbstractBaseUser.password
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_login = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
