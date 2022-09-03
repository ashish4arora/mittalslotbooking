from urllib.response import addclosehook
from django.shortcuts import render, redirect

from courts.models import Courts
from . import forms
from django.contrib import messages
from .models import Calendar, Days, Slots

def updateSlots(request):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    addslotform = forms.addSlot()
    makeCalendarform = forms.makeCalendar()
    if request.method == "POST":
        if request.POST.get('state') == "slotform":
            addslotform = forms.addSlot(request.POST)
            if addslotform.is_valid():
                addslotform.save()
            else:
                messages.error(request, "Error occurred while adding slot!")
        elif request.POST.get('state') == "calendarform":
            makeCalendarform = forms.makeCalendar(request.POST)
            if makeCalendarform.is_valid():
                makeCalendarform.save()
            else:
                messages.error(request, "Error occured while assigning the slot!")
                

    allslots = Slots.objects.all()
    calendar = Calendar.objects.all()
    # obj = Courts.objects.get(courtname = "Mittal Court Badminton")
    # temp = obj.calendar.filter(day = Days.objects.get(day = "Monday"))
    # slots = []
    # for i in temp:
    #     slots += [str(e) for e in i.slot.all()]
    # slots.sort()
    context = {'addslotform':addslotform, 'makecalendarform':makeCalendarform ,'allslots':allslots, 'calendar':calendar}
    return render(request, 'slots/updateSlots.html', context)

def removeSlots(request, pk):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    Slots.objects.get(id = pk).delete()
    return redirect('updateslots')

def removeAssignment(request, pk):
    if request.user.isAdmin == False:
        return redirect('accessdenied')
    Calendar.objects.get(id = pk).delete()
    return redirect('updateslots')