from decimal import Clamped
from django.forms import ModelForm
from django import forms
from .models import Slots, Calendar

class addSlot(ModelForm):
    start_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs = {'type':'time'}))
    end_time = forms.TimeField(widget=forms.widgets.TimeInput(attrs = {'type':'time'}))
    class Meta:
        model = Slots
        fields = '__all__'

class makeCalendar(ModelForm):
    class Meta:
        model = Calendar
        fields = ['court', 'slot', 'day']