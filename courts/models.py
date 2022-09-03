from django.db import models
from sports.models import Sports
# Create your models here.

class Courts(models.Model):
    courtname = models.CharField(max_length=12)
    courtlocation = models.CharField(max_length=60)
    sport = models.ForeignKey(Sports, related_name="courts", on_delete=models.CASCADE, null = True, blank = True)
    membership_req = models.CharField(max_length=5)

    def __str__(self):
        return self.courtname