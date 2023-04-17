from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

User = settings.AUTH_USER_MODEL


class Admin(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    primary_number = models.CharField(unique=True, max_length=10)
    secondary_number = models.CharField(unique=True, max_length=10)
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'Admin Table'

    def __str__(self):
        return self.first_name

