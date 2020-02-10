from django.db import models
# Create your models here.

class DTR(models.Model):
    date = models.DateField(null=True)
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)
    diff = models.DurationField(null=True)

class Account(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    dtr = models.ManyToManyField(DTR, blank=True)