from django.db import models
# Create your models here.

class DTR(models.Model):
    date = models.DateField(null=True)
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)
    diff = models.DurationField(null=True)