from email.policy import default
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =  ['first_name', 'last_name', 'username']