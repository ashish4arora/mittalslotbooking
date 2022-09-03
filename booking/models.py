from django.db import models
from slots.models import Slots
from Users.models import CustomUser
from courts.models import Courts
from sports.models import Sports
# Create your models here.


class Booking(models.Model):
    slot = models.ForeignKey(Slots, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, related_name="bookings", on_delete=models.CASCADE)
    court = models.ForeignKey(Courts, related_name="bookings", on_delete=models.CASCADE)
    sport = models.ForeignKey(Sports, related_name="bookings", on_delete=models.CASCADE)
    date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)
    waitlist = models.IntegerField()
    isConfirmed = models.BooleanField()

    def __str__(self):
        return str(self.slot) + " " + str(self.court)
