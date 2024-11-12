import requests
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    class Meta:
        db_table ='nilouser'