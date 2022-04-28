from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Hospital
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
        email = request.POST['email']
        password = request.POST['password']
        
        
        user = authenticate(email=email, password=password)
        
        
        if user is not None:
            return HttpResponse("got it from database")
            login(request, user)
            hospital_name = user.hospital_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "hospital/hospital_account.html",{"hospital_name":hospital_name})
        else:
            return HttpResponse("next")
            # messages.error(request, "You entered a wrong Username or Password!!! \n If your Hospital has no account on BloodLoof, Kindly email us @thebloodloof@gmail.com\n If you are a User who wish to Register, Click on 'Register' at the top bar.")
            return redirect('hospital_signin')
    
    return render(request, "hospital/hospital_signin.html")


def hospital_signin(request):
    return render(request, "hospital/hospital_signin.html")


def hospital_signout(request):
    logout(request)
    messages.success(request, "You are logged out!")
    return redirect ('home')