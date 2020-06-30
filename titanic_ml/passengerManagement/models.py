from django.db import models
from django.utils import timezone

# Create your models here.

class PassengerDB(models.Model):
    passenger_name = models.CharField(max_length=30)
    passenger_age = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)
    time_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s %s"%(self.passenger_name, self.completed)
