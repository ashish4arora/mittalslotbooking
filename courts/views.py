from decimal import Clamped
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Courts
from sports.models import Sports
from inventory.models import Inventory
from slots.models import Calendar
from . import forms
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def updateCourts(request):
    addcourtform = forms.addCourt()
    if request.method == "POST" and (request.user.isAdmin or request.user.status == "staff"):
        addcourtform = forms.addCourt(request.POST)
        if addcourtform.is_valid():
            courtdata = addcourtform.save(commit = False)
            courtdata.sport = Sports.objects.get(name = request.POST.get('sport'))
            courtdata.save()
            addcourtform = forms.addCourt()
        else:
            messages.error(request, "Error occurred while adding slot!")

    allcourts = Courts.objects.all()
    allsports = Sports.objects.all()
    context = {'addcourtform':addcourtform, 'allcourts':allcourts, 'allsports':allsports}
    return render(request, 'courts/updateCourts.html', context)

def removeCourts(request, pk):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    Courts.objects.get(id = pk).delete()
    return redirect('updatecourts')

@login_required(login_url='login')
def viewcourt(request,pk):
    court = Courts.objects.get(id = pk)
    inventory = Inventory.objects.filter(court = court)
    slots = Calendar.objects.filter(court = court)
    context = {'court':court, 'inventory':inventory, 'slots':slots}
    return render(request, 'courts/courtdisplay.html', context)

