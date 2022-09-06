from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inventory, Item
from courts.models import Courts
from sports.models import Sports
from . import forms

def updateInventory(request):
    if request.user.isAdmin == False and request.user.status != "staff":
        return redirect('accessdenied')
    additemform = forms.addItem()
    addinventoryform = forms.addInventory()
    if request.method == "POST":
        if request.POST.get('type') == "additem":
            additemform = forms.addItem(request.POST)
            if additemform.is_valid():
                itemdata = additemform.save(commit = False)
                itemdata.sport = Sports.objects.get(name = request.POST.get('sport'))
                itemdata.save()
                additemform = forms.addItem()
            else:
                messages.error(request, "Error occurred while adding item!")
                
        elif request.POST.get('type') == "addInventory":
            addinventoryform = forms.addInventory(request.POST)
            if addinventoryform.is_valid():
                invdata = addinventoryform.save(commit = False)
                invdata.item = Item.objects.get(itemname = request.POST.get('item'))
                invdata.court = Courts.objects.get(courtname = request.POST.get('court'))
                invdata.save()
                addinventoryform = forms.addInventory()
            else:
                messages.error(request, "Error occurred while adding inventory!")

    allsports = Sports.objects.all()
    allcourts = Courts.objects.all()
    allitems = Item.objects.all()
    allinventory = Inventory.objects.all()
    context = {'additemform':additemform, 'addinventoryform':addinventoryform, 'allsports':allsports, 'allcourts':allcourts, 'allitems':allitems, 'allinventory':allinventory}
    return render(request, 'inventory/updateInventory.html', context)

def removeInventory(request, pk):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    Inventory.objects.get(id = pk).delete()
    return redirect('updateinventory')

def removeItem(request, pk):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    Item.objects.get(id = pk).delete()
    return redirect('updateinventory')