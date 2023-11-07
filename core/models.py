from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator
from core.validations import validate_email
from core.manager import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True,validators=[EmailValidator(message="Invalid email format."),validate_email])
    # username = models.CharField(max_length=255,null=True,blank=True)
    
    # full_name = models.CharField(max_length=255)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']