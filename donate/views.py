from Bloodloof_project import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Donor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone
from authentication.views import user_account
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
            email = request.user.email
            fname = request.user.first_name
            full_name = request.user.full_name

        
        if Donor.objects.filter(username = username).exists():
            messages.error(request, "You can not make an apointment twice in less than 2 months")
            return redirect('home')
        
        
        if len(phone_number)>14:
            messages.error(request, "Phone Number can not exceed 14 characters")
            return redirect('donate')
        
        if len(weight)>6 :
            messages.error(request, "Kindly Make Sure Your weight is a 2-digits number with at most two decimals Ex: 62.50")
            return redirect('donate')
        
        if len(height)>4:
            messages.error(request, "Kindly Make Sure Your Height is a 1-digit number with at most two decimals Ex: 1.75")
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
        mydonor.password = password
        mydonor.height = height
        mydonor.available_time = available_time
        mydonor.address = address
        mydonor.hospital = hospital
        mydonor.username = username
        mydonor.full_name = full_name
        mydonor.is_active = True
        mydonor.save()
        
        messages.success(request, "You have registered for a Blood Donation session, You will receive a confirmation on your email")
        
        # Welcome Email
        subject = "Thank your for your blood donation initiative"
        message = "Hello " + fname+ "!! \n" + "We have received your sign up for blood donation, we will reach out within the next 24 hours with a confirmation \nThank you"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return render(request, "authentication/user_account.html")
        
    return render(request, "donate/donate.html")