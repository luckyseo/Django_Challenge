from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): #Customize!
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    name = models.CharField(max_length=150, default=False)
    is_host = models.BooleanField(default=False)
    def __str__(self):
        return self.name