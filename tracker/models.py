from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here
class volunteer_hour(models.Model):
    date = models.DateField()
    start = models.TimeField(default=None)
    end = models.TimeField(default=None)

    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('hours')
