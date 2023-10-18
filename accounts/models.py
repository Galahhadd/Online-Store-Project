from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

from .managers import CustomUserManager

class CustomUser(AbstractUser):
	username = None 
	email = models.EmailField(unique=True, max_length=255)
	phone_number = models.CharField(unique=True, max_length=20, validators=[RegexValidator])

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

	def __str__(self):
		return self.email