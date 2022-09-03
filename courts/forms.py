from django.forms import ModelForm
from .models import Courts, Sports
from django import forms
class addCourt(ModelForm):
    courtname = forms.CharField(label="Court Name")
    courtlocation = forms.CharField(label="Court Location")
    membership_req = forms.CharField(label = "Membership Code")
    class Meta:
        model = Courts
        fields = ['courtname', 'courtlocation', 'membership_req']