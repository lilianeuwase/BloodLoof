# Import Libraries
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from donate.models import Donor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Bloodloof_project import settings
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt
from json import dumps

# Create your views here.
def home(request):
    return render(request, "authentication/homepage.html")

# user_signup function will be used by Users and Hospitals to sign up to BloodLoof
def user_signup(request):
    
    if request.user.is_authenticated:
        user = request.user
        username = user.username
        fname = user.first_name
        messages.error(request, "You are logged in with another account, signout to resgister a new account")
        return redirect('user_account')
    
    elif request.method == "POST":
        username = request.POST['username'].lower()
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email'].lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        # Condition to verify if the username has been used before
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists, Please choose another username")
            return redirect('user_signup')
        
        # Condition to verify if the email has been used before
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already exists, Please sign in if you already has an account")
            return redirect('user_signup')
        
        # Condition to make sure that the username does not exceed 10 characters
        if len(username)>10:
            messages.error(request, "Username can not exceed 10 characters")
            return redirect('user_signup')
        
        # Condition to verify if the 2 passwords match  
        if password1 !=password2:
            messages.error(request, "Passwords do not match")
            return redirect('user_signup')
        
        # Condition to make sure the username box is not empty 
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('user_signup')
        
        
        # If all conditions are checked the user is then saved
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        
        messages.success(request, "Account Successfully Created!!")
        
        # Welcome Email after saving the user's info
        subject = "Welcome to BloodLoof Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to BloodLoof!! \nThank you"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently = True)
        return redirect('user_signin')
        
    return render(request, "authentication/user_signup.html")

def user_signin(request):
    return render(request, "authentication/user_signin.html")

# user_signout function will be used by Users and Hospitals to signout to BloodLoof
def user_signout(request):
    logout(request)
    messages.success(request, "You are logged out!")
    return redirect ('home')

# user_account function will be used by Users and Hospitals to navigate their accounts
@csrf_exempt
def user_account(request, *args, **kwargs):
    print(args, kwargs)
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            if user.is_staff == False:
                login(request, user)
                fname = user.first_name
                messages.success(request, "Logged In Sucessfully!!")
                return render(request, "authentication/user_account.html",{"fname":fname})
            
            elif user.is_staff == True:
                login(request, user)
                hospital_name = user.username.lower()
                messages.success(request, "Logged In Sucessfully!!")
                
                # Get Donors' list
                butaro_list = list(filter(None,Donor.objects.filter(hospital='Butaro District Hospital').values_list('donated', 'phone_number', 'weight', 'height', 'available_time', 'dob', 'address', 'full_name')))
                musanze_list = list(filter(None,Donor.objects.filter(hospital='Musanze District Hospital').values_list('donated', 'phone_number', 'weight', 'height', 'available_time', 'dob', 'address', 'full_name')))
                faisal_list = list(filter(None,Donor.objects.filter(hospital='King Faisal Hospital').values_list('donated', 'phone_number', 'weight', 'height', 'available_time', 'dob', 'address', 'full_name')))

                
                #Pass data to the table template
                if(hospital_name == 'butaro_hospital'):
                    
                    hospital ='Butaro District Hospital'
                    return render(request, "hospital/hospital_account.html",{"hospital_list":butaro_list, "hospital":hospital})
                
                elif(hospital_name == 'musanze_hospital'):
                    
                    hospital ='Musanze District Hospital'
                    return render(request, "hospital/hospital_account.html",{"hospital_list":musanze_list, "hospital":hospital})
                
                elif(hospital_name == 'faisal_hospital'):
                    
                    hospital ='King Faisal Hospital'
                    return render(request, "hospital/hospital_account.html",{"hospital_list":faisal_list, "hospital":hospital})

                
        else:
            messages.error(request, "You entered a wrong Username or Password!!! \n Sign Up If you do not have an account!!!, for hospital sign ups kindly email us @thebloodloof@gmail.com")
            return redirect('user_signin')
        
    elif request.user.is_authenticated:
        user = request.user
        if user is not None:
            if user.is_staff == False:
                login(request, user)
                fname = user.first_name
                return render(request, "authentication/user_account.html",{"fname":fname})
            
            elif user.is_staff == True:
                login(request, user)
                hospital_name = user.username.lower()
                
                # Get Donors' list
                butaro_list = list(filter(None,Donor.objects.filter(hospital='Butaro District Hospital').values_list('donated', 'phone_number', 'weight', 'height', 'available_time', 'dob', 'address', 'full_name')))
                musanze_list = list(filter(None,Donor.objects.filter(hospital='Musanze District Hospital').values_list('donated', 'phone_number', 'weight', 'height', 'available_time', 'dob', 'address', 'full_name')))
                faisal_list = list(filter(None,Donor.objects.filter(hospital='King Faisal Hospital').values_list('donated', 'phone_number', 'weight', 'height', 'available_time', 'dob', 'address', 'full_name')))

                
                #Pass data to the table template
                if(hospital_name == 'butaro_hospital'):
                    
                    hospital ='Butaro District Hospital'
                    return render(request, "hospital/hospital_account.html",{"hospital_list":butaro_list, "hospital":hospital})
                
                elif(hospital_name == 'musanze_hospital'):
                    
                    hospital ='Musanze District Hospital'
                    return render(request, "hospital/hospital_account.html",{"hospital_list":musanze_list, "hospital":hospital})
                
                elif(hospital_name == 'faisal_hospital'):
                    
                    hospital ='King Faisal Hospital'
                    return render(request, "hospital/hospital_account.html",{"hospital_list":faisal_list, "hospital":hospital})
    
    return render(request, "authentication/user_signin.html")


# Error functions will be used to deal with the 404, 500, 403 and 400 errors
def error_404(request, exception):
    return render(request, 'errors/404.html')

def error_500(request, exception=None):
    return render(request, "errors/500.html", {})

def error_403(request, exception=None):
    return render(request, "errors/403.html", {})

def error_400(request, exception=None):
    return render(request, "errors/400.html", {})

# change_password function will be used by Users and Hospitals to change passwords of their BloodLoof accounts
def change_password_page(request, *args, **kwargs):
    return render(request, 'authentication/change_password_page.html')

def change_password(request, *args, **kwargs):
    print(args, kwargs)
    
    if request.method == 'POST':
        username = request.POST['username']
        newpassword = request.POST['newpassword']
        newpassword1 = request.POST['newpassword1']
        
        if (newpassword != newpassword1):
            messages.error(request, "Password does not match")
            return redirect('change_password_page')
            
        else:
            myuser = User.objects.get(username=username)
            myuser.set_password(newpassword)
            myuser.save()
            
            messages.success(request, "Password Changed!!")
            return redirect('user_signin')
    