from django.http import HttpResponse
from django.shortcuts import redirect, render
# from .models import Hospital
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
from datetime import date, datetime
from decimal import Decimal

# Create your views here.

def hospital_account(request, *args, **kwargs):
    print(args, kwargs)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(username=username, password=password)
        
        if user is not None and user.is_staff == True:
            login(request, user)
            hospital_name = user.username
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/user_account.html",{"fname":hospital_name})
        else:
            # return HttpResponse("If You are a regular user kindly sign up, If you are a hospital and wish to sign up kindly email us @thebloodloof@gmail.com")
            messages.error(request, "If You are a regular user kindly sign up, If you are a hospital and wish to sign up kindly email us @thebloodloof@gmail.com")
            return redirect('hospital_signin')
    
    return render(request, "hospital/hospital_signin.html")


def hospital_signin(request):
    return render(request, "hospital/hospital_signin.html")


def hospital_signout(request):
    logout(request)
    messages.success(request, "You are logged out!")
    return redirect ('home')