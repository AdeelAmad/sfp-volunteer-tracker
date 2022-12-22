from django.contrib.auth.models import User
from users.models import volunteer
from django.db import models
from django.urls import reverse


# Create your models here
class volunteer_hour(models.Model):
    date = models.DateField()
    start = models.TimeField(default=None)
    end = models.TimeField(default=None, null=True)

    volunteer = models.ForeignKey(volunteer, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('hours')
