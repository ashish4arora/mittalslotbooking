from django.db import models
from sports.models import Sports
from courts.models import Courts
# Create your models here.

class Item(models.Model):
    itemname = models.CharField(max_length=25)
    sport = models.ForeignKey(Sports, related_name="inventory", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.itemname

class Inventory(models.Model):
    item = models.ForeignKey(Item, related_name="inventory", on_delete=models.CASCADE, null = True, blank=True)
    count = models.IntegerField()
    court = models.ForeignKey(Courts, related_name="inventory", on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return self.item.itemname + " " + str(self.count)