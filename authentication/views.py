from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from donate.models import Donor
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Bloodloof_project import settings
from django.core.mail import send_mail, EmailMessage
from django.views.decorators.csrf import csrf_exempt

# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your views here.
def home(request):
    return render(request, "authentication/homepage.html")

def user_signup(request):
    
    if request.method == "POST":
        username = request.POST['username'].lower()
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email'].lower()
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if User.objects.filter(username = username):
            messages.error(request, "Username already exists, Please choose another username")
            return redirect('user_signup')
        
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already exists, Please sign in if you already has an account")
            return redirect('user_signup')
        
        # if User.objects.filter(number = number).exists():
        #     messages.error(request, "Phone number already exists, Please sign in if you already has an account")
        #     return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username can not exceed 10 characters")
            return redirect('user_signup')
            
        if password1 !=password2:
            messages.error(request, "Passwords do not match")
            return redirect('user_signup')
            
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('user_signup')
            
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = True
        myuser.save()
        
        messages.success(request, "Account Successfully Created!!")
        
        # Welcome Email
        subject = "Welcome to BloodLoof Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to BloodLoof!! \nThank you"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        return redirect('user_signin')
        
    return render(request, "authentication/user_signup.html")

def user_signin(request):
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
    
    return render(request, "authentication/user_signin.html")

def user_signout(request):
    logout(request)
    messages.success(request, "You are logged out!")
    return redirect ('home')

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
                musanze_list = list(filter(None,Donor.objects.filter(hospital='Musanze District Hospital').values_list('username', flat=True)))
                faisal_list = list(filter(None,Donor.objects.filter(hospital='King Faisal Hospital').values_list('username', flat=True)))
                
                if(hospital_name == 'butaro_hospital'):
                    n=0
                    for i in butaro_list:
                        donor_donated = butaro_list[n][0]
                        donor_phone_number = butaro_list[n][1]
                        donor_weight = butaro_list[n][2]
                        donor_height = butaro_list[n][3]
                        donor_available_time = butaro_list[n][4]
                        donor_dob = butaro_list[n][5]
                        donor_address = butaro_list[n][6]
                        donor_full_name = butaro_list[n][7]
                        donor_hospital='Butaro District Hospital'
                        n=+1
                        loop_n = ""+"a"
                            
                        return render(request, "hospital/hospital_account.html",{"donor_donated":donor_donated,
                                                                                 "donor_full_name":donor_full_name,
                                                                             "donor_phone_number":donor_phone_number,
                                                                             "donor_weight":donor_weight,
                                                                             "donor_height":donor_height,
                                                                             "donor_available_time":donor_available_time,
                                                                             "donor_dob":donor_dob,
                                                                             "donor_address":donor_address,
                                                                             "donor_hospital":donor_hospital,
                                                                             "n":n})
                    return render(request, "hospital/hospital_account.html", {"loop_n":loop_n})
                
                elif(hospital_name == 'musanze_hospital'):
                    return render(request, "hospital/hospital_account.html",{"hospital_name":hospital_name}, {"hospital_list":musanze_list})
                
                elif(hospital_name == 'faisal_hospital'):
                    return render(request, "hospital/hospital_account.html",{"hospital_name":hospital_name}, {"hospital_list":faisal_list})
                
        else:
            messages.error(request, "You entered a wrong Username or Password!!! \n Sign Up If you do not have an account!!!, for hospital sign ups kindly email us @thebloodloof")
            return redirect('user_signin')
    
    return render(request, "authentication/user_signin.html")

# def continue_page(request, *args, **kwargs):
#     print(args, kwargs)
    
#     user = authenticate(username=user_account.username, password=user_account.password1)
#     if request.method == 'POST':
#         if user.is_staff == False:
#             return render(request, "authentication/user_account.html")
#         else:
#             return render(request, "hospital/hospital_account.html")

def error_404(request, exception):
    return render(request, 'errors/404.html')

def error_500(request, exception=None):
    return render(request, "errors/500.html", {})

def error_403(request, exception=None):
    return render(request, "errors/403.html", {})

def error_400(request, exception=None):
    return render(request, "errors/400.html", {})

def change_password(request, *args, **kwargs):
    print(args, kwargs)
    myuser = User.objects.get(username='john')
    myuser.set_password('new password')
    myuser.save()
    
   
    
# def donate(request):
#     if request.method == "POST":
#         dob = request.POST['dob']
#         kgs = request.POST['kgs']
#         height = request.POST['height']
#         schedule = request.POST['schedule']
#         return HttpResponse(dob)
        
#     return render(request, "authentication/donate.html")
        
    

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