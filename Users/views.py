from django.shortcuts import render, redirect
from . import forms
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def landing(request):
    return redirect('home')

def loginuser(request):
    page = 'login'

    if request.method == "POST":
        username = request.POST.get('username').lower()

        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username = username)
        except:
            messages.error(request, "User does not exist!")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password does not match")

    context = {'page':page}
    return render(request, 'Users/login_register.html', context)
        

def register(request):
    page = 'register'
    form = forms.CustomUserCreationForm()
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            formresponse = form.save(commit=False)
            formresponse.username = formresponse.username.lower()
            username = formresponse.username.lower()
            password = formresponse.password
            formresponse.save()
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occured")
    context = {'page':page, 'form':form}
    return render(request, 'Users/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('landing')

def home(request):
    context = {}
    return render(request, 'Users/home.html' , context)

def accessdenied(request):
    return render(request, 'Users/accessdenied.html')

def assignstaff(request):
    success = False
    if request.method == "POST":
        username = request.POST.get('username')
        user = CustomUser.objects.get(username = username)
        if user is not None:
            if user.status == "staff":
                messages.error(request, "The user already has staff status")
            else:
                user.status = "staff"
                user.save()
                success = True
        else:
            messages.error(request, "User does not exist")
    staffers = CustomUser.objects.filter(status = "staff")
    context = {'success': success, 'staffers' : staffers}

    return render(request, 'Users/assignstaff.html', context)

def revokestaff(request, pk):
    user = CustomUser.objects.get(username = pk)
    user.status = "student"
    user.save()
    return redirect('assignstaff')