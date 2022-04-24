from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Donor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
from authentication.views import signin_user
from django.contrib.auth.models import User
from datetime import date, datetime
from decimal import Decimal

# Create your views here.

def donate(request):
    
    now = datetime.now()
    
    if request.method == "POST":
        phone_number = request.POST['phone_number']
        dob = request.POST['dob']
        weight = request.POST['weight']
        height = request.POST['height']
        available_time = request.POST['available_time']
        hospital = request.POST['hospital']
        address = request.POST['address']
        
        if request.user.is_authenticated:
            username = request.user.username
            password = request.user.password
            
        # def calculate_age(dob):
        #     today = date.today()
        #     age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        #     return age
        
        
        if Donor.objects.filter(phone_number = phone_number).exists():
            messages.error(request, "You can not make an apointment twice")
            return redirect('home')
        
        
        if len(phone_number)>14:
            messages.error(request, "Phone Number can not exceed 14 characters")
            return redirect('donate')
        
        if (datetime.strptime(available_time, '%Y-%m-%dT%H:%M') < now + timezone.timedelta(days=1)):
            messages.error(request, "You can only book an apointment for the next day or later")
            return redirect('donate')
        
        #Calculate the donor's Age
        today = date.today()
        birthdate = datetime.strptime(dob, '%Y-%m-%d')
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        HttpResponse(age)
        
        if age<18:
            messages.error(request, "Only 18 years of age and above can donate blood")
            return redirect('donate')
        
        if Decimal(weight)<49.9:
            messages.error(request, "You need to weight 50kgs or more to donate blood")
            return redirect('donate')
            
            
        mydonor = Donor.objects.create_user(phone_number, dob)
        
        mydonor.weight = weight
        mydonor.height = height
        mydonor.available_time = available_time
        mydonor.username = username
        mydonor.password = password
        mydonor.address = address
        mydonor.hospital = hospital
        mydonor.is_active = True
        mydonor.save()
        
        messages.success(request, "You have registered for a Blood Donation session, You will receive a confirmation on your email")
        return render(request, "authentication/user.html")
        
        # Welcome and Confirmation Email
        
        # Welcome Email
        # subject = "Welcome to BloodLoof Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to BloodLoof!! \nThank you"        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        # return redirect('signin_user')
        
    return render(request, "donate/donate.html")