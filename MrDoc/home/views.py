from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import NearBy_Doctor, Appointment_List, departments, doctorAccount
from django.contrib import messages

# for user authticcation 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as authlogin,logout
# email
# from MrDoc import settings
# from django.core.mail import send_mail
from email.message import EmailMessage
import ssl
import smtplib



# Create your views here.
def home(request):
    # this form is accessing for taking appointment list from home page
    if request.method == "POST":
        depName = request.POST.get("sedep")
        Pname = request.POST.get("name")
        Pmail = request.POST.get("mail")
        docName = request.POST.get("sedoc")
        Pphone = request.POST.get("phone")
        AppointDate = request.POST.get("date")

        appointment_list = Appointment_List(se_dept = depName, se_doc = docName, patient_name = Pname, patient_phone = Pphone, patient_email = Pmail, calendar = AppointDate)
        appointment_list.save()

        # SEND EMAIL
        email_sender = 'sa3518548@gmail.com'
        email_password = 'pziggqxkwggxtopt'

        email_receiver = Pmail
        subject = "hello "+Pname+"! check your appointment status."
        body = "Hi "+ Pname+ " your appointment is booked.\nthanking you team malloc to visit our doctor appointment system.\nDoctor name: "+docName +"\nDepartment: "+depName+"\nappointment date: "+AppointDate

            

            
            
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
            smtp.login(email_sender,email_password)
            smtp.sendmail(email_sender,email_receiver,em.as_string())





        messages.success(request,"Your Appointment is booked, we send a mail on your mail address. Please check it out and Thank you!")


    return render(request,'index.html',{'doc':NearBy_Doctor.objects.all(), 'dep':departments.objects.all()})
    # return HttpResponse('this is home page')


def about(request):
    fn = User.first_name
    return render(request,'about.html',{'fname':fn})

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
        my_user.username = uname

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
            messages.success(request,'Thank You! Your are successfully logged in. Now you can create your desired account.')
            return render(request, 'index.html', {'fname':fname})
        
        else:
            messages.error(request, 'Bad request! Username or Password did not match. Try aging.')
            return redirect('login')


    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('home')


# for doctor account
def doctorAcc(request):
    uname = None
    he = None
    if request.method == "POST":
        usname = request.POST.get("username")
        name = request.POST.get("name")
        depname = request.POST.get("dep")
        clinic = request.POST.get("cli")
        degree = request.POST.get("deg")
        district = request.POST.get("dis")
        charge = request.POST.get("char")
        language = request.POST.get("lang")

        uname = usname

        docAcc = doctorAccount(username=usname,name=name,depName=depname,Clinic=clinic,Degree=degree,district=district,charge=charge,langauge=language)
        docAcc.save()


    he = User.USERNAME_FIELD.title
    print(he)
    if he == uname:
        messages.success(request,"Your account is successfully created")
        return render(request,'doctorAcc.html')
    else:
        messages.error(request,"username did not match. Pleasse try again! ")
        return redirect('home')
    

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

def contact(request):
    
    return render(request, 'contact.html')
    # return HttpResponse('this is contact page')

def base(request):
    
    return render(request,'base.html')

def review(request):
    return render(request,'review.html')


