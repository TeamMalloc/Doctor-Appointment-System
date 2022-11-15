from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import NearBy_Doctor
from django.contrib import messages

# for user authticcation 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout



# Create your views here.
def home(request):
    return render(request,'index.html')
    # return HttpResponse('this is home page')

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')
    # return HttpResponse('this is services page')

def signUp(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        fpass = request.POST.get("pass1")
        cpass = request.POST.get("pass2")

        # validation for user
        if User.objects.filter(username=uname):
            messages.error(request,"Username already exist!")
            return redirect('signUp')

        if User.objects.filter(email=email):
            messages.error(request,"email already registerd")
            return redirect('signUp')

        if len(uname) >10:
            messages.error(request,"the username must be under 10 character!")
            return redirect('signUp')

        if fpass != cpass:
            messages.error(request,"Passwords didn't match.Try agian!")
            return redirect('signUp')

        if not uname.isalnum():
            messages.error(request,"Username must be alpha-numeric!")
            return redirect('signUp')
        


        my_user = User.objects.create_user(uname,email,fpass)
        my_user.first_name = fname
        my_user.last_name = lname

        my_user.save()

        messages.success(request, 'Thank you! your account has been successfully created.')

        return redirect('login')

        

        # regusers = RegUsers(UserName=uname, Fname=fname, Lname=lname, Email=email, Password=fpass, CPassword=cpass, Date=datetime.today())
        # regusers.save()
        # confirmation message

        # return redirect('login')
    return render(request,'signUp.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass1")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            authlogin(request, user)
            fname = user.first_name
            return render(request, 'doctorAcc.html', {'fname':fname})
        
        else:
            messages.error(request, 'Bad request! Username or Password did not match. Try aging.')
            return redirect('login')


    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('home')

def base(request):
    fname = User.first_name
    return render(request,'base.html',{'fname':fname})

# for doctor account
def doctorAcc(request):
    return render(request,'doctorAcc.html')

# for NearByDoc
def NearByDoc(request):
    nr = None
    if request.method == "POST":
        nearby = request.POST.get("NearBy")
        nr = nearby
    return render(request,'nearbyDoc.html',{'nrb':NearBy_Doctor.objects.all(),'near':nr})
    
#for Emergency Doctor
def emDoc(request):
    wkh = "Emergency doc"

    return render(request,'emDoc.html',{'em':NearBy_Doctor.objects.all(),'wkh':wkh})
