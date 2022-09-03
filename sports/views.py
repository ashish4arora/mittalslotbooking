from django.shortcuts import render, redirect
from django.contrib import messages
from courts.models import Courts
from sports.models import Sports
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url='login')
def updateSports(request):
    addsportform = forms.addSport()
    if request.method == "POST" and (request.user.isAdmin or request.user.status == "staff") :
        addsportform = forms.addSport(request.POST)
        if addsportform.is_valid():
            addsportform.save()
        else:
            messages.error(request, "Error occurred while adding sport!")

    allsports = Sports.objects.all()
    context = {'addsportform':addsportform, 'allsports':allsports}
    return render(request, 'sports/updateSports.html', context)

def removeSports(request, pk):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    Sports.objects.get(sportcode = pk).delete()
    return redirect('updatesports')

@login_required(login_url='login')
def viewsport(request, pk):
    sport = Sports.objects.get(sportcode = pk)
    courts = Courts.objects.filter(sport = sport)
    context = {'courts':courts, 'sport':sport}
    return render(request, 'sports/sportdisplay.html', context)
