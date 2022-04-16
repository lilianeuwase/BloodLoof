from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Bloodloof_project import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token


# Create your views here.
def home(request):
    return render(request, "authentication/homepage.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists, Please choose another username")
            return redirect('home')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already exists, Please sign in if you already has an account")
            return redirect('home')
        
        # if User.objects.filter(number = number).exists():
        #     messages.error(request, "Phone number already exists, Please sign in if you already has an account")
        #     return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username can not exceed 10 characters")
            return redirect('home')
            
        if password1 !=password2:
            messages.error(request, "Passwords do not match")
            return redirect('home')
            
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
            
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.phone_number = phone_number
        myuser.is_active = True
        myuser.save()
        
        messages.success(request, "Account Successfully Created!!")
        
        # Welcome and Confirmation Email
        
        # Welcome Email
        subject = "Welcome to BloodLoof Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to BloodLoof!! \nThank you"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('signin')
        
    return render(request, "authentication/signup.html")

def signin(request):
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
        
    #     user = authenticate(username=username, password=password1)
        
    #     if user is not None:
    #         login(request, user)
    #         fname = user.first_name
    #         #messages.success(request, "Logged In Sucessfully!!")
    #         return render(request, "authentication/user.html",{"fname":fname})
    #     else:
    #         messages.error(request, "You entered a wrong Username or Password!!! \n Sign Up If you do not have an account!!!")
    #         return redirect('signin')
    
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    # messages.success(request, "You are logged out!")
    return redirect ('home')

def signin_user(request, *args, **kwargs):
    print(args, kwargs)
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            #messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/user.html",{"fname":fname})
        else:
            messages.error(request, "You entered a wrong Username or Password!!! \n Sign Up If you do not have an account!!!")
            return redirect('signin')
    
    return render(request, "authentication/signin.html")
    
   
    
def donate(request):
    if request.method == "POST":
        dob = request.POST['dob']
        kgs = request.POST['kgs']
        height = request.POST['height']
        schedule = request.POST['schedule']
        return HttpResponse(dob)
        
    return render(request, "authentication/donate.html")
        
    

# def activate(request, uidb64, token):
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
        
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         myuser = None
        
#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_activate = True
#         myuser.save()
#         login(request, myuser)
#         return redirect('home')
    
#     else:
#         return render(request, 'activation_failed.html')