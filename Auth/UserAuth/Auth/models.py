from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserModel(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email