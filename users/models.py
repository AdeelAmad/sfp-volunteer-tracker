from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_id = models.CharField(max_length=10, default=None)