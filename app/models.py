from django.db import models
# Create your models here.

class DTR(models.Model):
    date = models.DateField(null=True)
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)
    desc = models.CharField(max_length=512, null=True)
    diff = models.DurationField(null=True)

    class Meta:
        db_table = 'dtr'

    def __str__(self):
        return str(self.date) + " " + str(self.time_in) + " " + str(self.time_out)

class Account(models.Model):
    username = models.CharField(max_length=255, null=True, blank=True)
    dtr = models.ManyToManyField(DTR, blank=True, related_name="dtr")
    fuck=models.ManyToManyField(DTR, blank=True, related_name="fuck")

    class Meta:
        db_table = 'account'

    def __str__(self):
        return self.username