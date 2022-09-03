from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    username = models.CharField(max_length=11, primary_key=True)
    membershipcode = models.CharField(max_length=5, default="FREE")
    status = models.CharField(max_length=10, default="student")
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

