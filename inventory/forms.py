from ast import In
from django.forms import ModelForm
from .models import Inventory, Item
from django import forms

class addItem(ModelForm):
    itemname = forms.CharField(label="Item Name")
    class Meta:
        model = Item
        fields = ['itemname']

class addInventory(ModelForm):
    count = forms.IntegerField(label = "Item Count")
    class Meta:
        model = Inventory
        fields = ['count']