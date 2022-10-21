from email import message
from pydoc import doc
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from DoctorAppSystem import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, "RegLoginSystem/index.html")

def userRole(request):
    return render(request,"RegLoginSystem/userRole.html")

def registration(request):
    
    if request.method == "POST":       
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(username=username):
        #     messages.error = (request,"user name already accessed! Please try another.")
        #     return redirect('home')
        # if User.objects.filter(email=email):
        #     messages.error = (request,"email already registered! Please try another.")
        #     return redirect("home")
        
        # if len(username)>10:
        #     messages.error(request,"username must be under 10 characters")
        
        # if pass1 != pass2:
        #     messages.error = (request, "Passwords did not match")
        
        # if not username.isalnum():
        #     messages.error = (request,"User name must be alpha numeric")
        #     return redirect('home')

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.conpass = pass2

        myuser.save()
        
        

        # message
        messages.success = (request,"your account has been successfully created. We have sent you a confirmation email. check it")

        # Email message
        subject = "welcome to Doctor Appoinment system"
        message = "Hello "+myuser.first_name+"\n"+"Thank Your For visiting our website. \n We have also sent a confirmation email, Please confirm your email in order to activate your account. "
        from_email = settings.EMAIL_HOST_USER
        to_lsit = [myuser.email]

        send_mail(subject,message,from_email,to_lsit,fail_silently=True)


        return redirect('signin')
  

    return render(request,"RegLoginSystem/reg.html")

def signin(request):
    if request.method == "POST":    
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"RegLoginSystem/userRole.html",{'fname' : fname})
        else:
            messages.error(request,"Bad request!try agian.")
            return redirect('home')
   


    return render(request,"RegLoginSystem/signin.html")

def signout(request):
    logout(request)
    # messages.success(request,"you are successfully loged out")
    return redirect('userRole')

def doctorRole(request):
    return render(request,"RegLoginSystem/doctorRole.html")

def patientRole(request):
    return render(request,"RegLoginSystem/patientRole.html")



