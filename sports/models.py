from pickle import TRUE
from django.db import models

class Sports(models.Model):
    sportcode = models.CharField(primary_key=True, max_length=3, blank = False)
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
        