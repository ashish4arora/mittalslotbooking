from multiprocessing.connection import wait
from django.shortcuts import render, redirect
from .models import Booking
from sports.models import Sports
from courts.models import Courts
from slots.models import Slots, Calendar, Days
from inventory.models import Inventory
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def updateBooking(request):
    allsports = Sports.objects.all()
    date = datetime.datetime.now().strftime("%x")
    day  = datetime.datetime.now().strftime("%A")
    time = datetime.datetime.now().strftime("%X")
    bookedslots = Booking.objects.filter(user = request.user)
    state = "sportfield"
    context = {'allsports' : allsports, 'day':day, 'date':date, 'time':time, 'state':state, 'bookedslots':bookedslots}
    if request.method == "POST":
        if request.POST.get('state') == "sportfield":
            allcourts = Courts.objects.filter(sport = Sports.objects.get(name = request.POST.get('sport')))
            context['state'] = "courtfield"
            context['sportvalue'] = request.POST.get('sport')
            context['allcourts'] = allcourts

        elif request.POST.get('state') == "courtfield":
            context['sportvalue'] = request.POST.get('sport')
            context['courtvalue'] = request.POST.get('court')
            context['state'] = "slotfield"
            calendar = Calendar.objects.filter(court = Courts.objects.get(courtname = context['courtvalue']), day = Days.objects.get(day = day))
            allslots = []
            for each in calendar:
                allslots += each.slot.all()
            allslots = list(set(allslots))
            context['allslots'] = allslots

        elif request.POST.get('state') == "slotfield":
            try:
                slot = Slots.objects.get(id = request.POST.get('slot'))
            except:
                messages.error(request, "Slot doesnt exist or no slot chosen")
                return redirect('updatebooking')
            court = Courts.objects.get(courtname = request.POST.get('court'))
            sport = court.sport
            waitlist = slot.bookings.filter(court = court).count()
            if waitlist == 0:
                isConfirmed = True
            else:
                isConfirmed = False
            if slot.bookings.filter(court = court, user = request.user).count():
                messages.error(request, "You have already booked this slot!")
            else:
                newbooking = Booking(slot = slot, user = request.user, court = court, sport = sport, date = datetime.date.today(), isConfirmed = isConfirmed, waitlist = waitlist)
                newbooking.save()
                messages.success(request, "Request Saved")
        
    return render(request, 'booking/booking.html', context)

@login_required(login_url='login')
def removeBooking(request, pk):
    obj = Booking.objects.get(id = pk)
    slot = obj.slot
    court = obj.court
    obj.delete()
    otherobj = Booking.objects.filter(slot = slot, court = court)
    for each in otherobj:
        print(each.user.username)
        print(each.waitlist)
        each.waitlist = each.waitlist -1
        each.save()
        if each.waitlist == 0:
            each.isConfirmed = True
            each.save()

    return redirect('updatebooking')
