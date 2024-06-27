
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=60)
    last_name=models.CharField(max_length=60)
    password=models.CharField(max_length=60)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
