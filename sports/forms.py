from django.forms import ModelForm
from .models import Sports
from django import forms
class addSport(ModelForm):
    sportcode = forms.CharField(label="Sport Code", max_length=3)
    name = forms.CharField(label="Sport Name")
    class Meta:
        model = Sports
        fields = '__all__'