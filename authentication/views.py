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
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists, Please choose another username")
            return redirect('home')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already exists, Please sign in if you already has an account")
            return redirect('signin')
        
        if len(username)>10:
            messages.error(request, "Username can not exceed 10 characters")
            
        if password1 !=password2:
            messages.error(request, "Passwords do not match")
            
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')
            
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        
        messages.success(request, "Account Successfully Created!!")
        
        # Welcome and Confirmation Email
        
        current_site = get_current_site(request)
        
        subject = "Welcome to BloodLoof login"
        message = render_to_string ('email_confirmation.html',{dict},{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        
        email = EmailMessage(
            subject, message,
            settings.EMAIL_HOST_USER, [myuser.email],
        )
        
        email.fail_silently = True
        email.send()
        
        # "Hello " +myuser.first_name + "!! \n" + "Welcome to BloodLoof, Thank you for registering.\n Kindly confirm your email address"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('signin')
        
    return render(request, "authentication/signup.html")

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        
        user = authenticate(username=username, password=password1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname': fname})
            
        else:
            messages.error(request, "Invalig login details!")
            return redirect('home')
        
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "You are logged out!")
    return redirect ('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
        
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
        
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_activate = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    
    else:
        return render(request, 'activation_failed.html')