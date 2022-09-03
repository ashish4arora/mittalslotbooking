from pickle import TRUE
from django.db import models
from courts.models import Courts

class Days(models.Model):
    day = models.CharField(max_length=10)
    
    def __str__(self):
        return self.day

class Slots(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.start_time) + " - " + str(self.end_time)

class Calendar(models.Model):
    court = models.ForeignKey(Courts, related_name="calendar", on_delete=models.CASCADE)
    slot = models.ManyToManyField(Slots, related_name="calendar")
    day = models.ManyToManyField(Days, related_name="calendar")
    date = models.DateField(null=True, blank= True)

    def __str__(self):
        return str(self.id)