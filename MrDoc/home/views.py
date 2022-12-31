from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import NearBy_Doctor, Appointment_List, departments
from django.contrib import messages
# from home.models import Faq
from .forms import FAQForm
from .forms import AnswerForm
from django.shortcuts import get_object_or_404

# for patient list
from .models import PatientList
from .models import patient


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
        doc_pat = request.POST.get("doc_pat")

        user = authenticate(request, username = username, password = password)
        if user is not None:
            authlogin(request, user)
            fname = user.first_name
            messages.success(request,'Thank You! Your are successfully logged in. Now you can create your desired account.')
            doc='Doctor'
            pat='Patient'

            if doc == doc_pat:
                return render(request, 'doctorAcc.html', {'fname':fname})
            else:
                return render(request, 'patientAcc.html', {'fname':fname})
            
        
        else:
            messages.error(request, 'Bad request! Username or Password did not match. Try aging.')
            return redirect('login')


    return render(request,'login.html')

def signout(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('home')

def patientAcc(request):
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            pat_image = request.POST.get("pat_image")
            if len(request.FILES) !=0:
                pat_image= request.FILES['pat_image']
            
            pat_name = request.POST.get("pat_name")
            pat_age = request.POST.get("pat_age")
            pat_location = request.POST.get("pat_location")
            pat_lag_spoken = request.POST.get("pat_lag_spoken")
            pat_occu = request.POST.get("pat_occu")
            


            # pat_name = user.first_name
            pat_obj = patient(pat_image = pat_image, pat_name = pat_name, pat_age=pat_age,pat_location = pat_location,pat_lag_spoken = pat_lag_spoken,
            pat_occu = pat_occu)
            pat_obj.save()
        
            return render (request,'patientAcc.html',{'pat_image':pat_image,'pat_name':pat_name,'pat_age':pat_age,'pat_location':pat_location,'pat_lag_spoken':pat_lag_spoken,'pat_occu':pat_occu})
        elif request.POST.get("form_type") == 'formTwo':
            blood = request.POST.get("blood")
            bllod_2 = request.POST.get("bllod_2")
            suger_lvl = request.POST.get("suger_lvl")
            dat=datetime.today()

            pat_health = health(blood=blood,bllod_2=bllod_2,suger_lvl=suger_lvl,date=dat)

            if int(blood) > 120 and int(bllod_2) > 80:
                condition='High BP!!';
            elif int(blood) < 120 and int(bllod_2) < 80:
                condition='low BP!!';
            elif int(blood) > 120 and int(bllod_2) < 80 or int(blood) < 120 and int(bllod_2) > 80:
                condition='Critical conditio';
                
            

            
            pat_health.save()
            return TemplateResponse (request,'patientAcc.html',{'blood':blood,'bllod_2':bllod_2,'suger_lvl':suger_lvl, 'condition':condition})

        
    return render (request,'patientAcc.html')
    # fname = user.first_name
    
    # print(user)
        
    

    


# for doctor account
def doctorAcc(request):
    return render(request,'doctorAcc.html', {'patients': patient.objects.all()})

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
    if request.method == "POST":
        na = request.POST.get("name")
        revi = request.POST.get("rev")
        dat=datetime.today()
        RE = reviewers(name=na,reviews=revi,time=dat)
        RE.save()
        return TemplateResponse(request, 'index.html', {"re":reviewers.objects.all()})
    return render(request,'review.html',)

def rateing(request):
    obj = rating.objects.filter(score=0).order_by("?").first()
    context={
        "obj" : obj,
    }

    return render(request,'rateing.html',context)

        

#--- FAQ Section for user ----#
def faq(request):
    # # faqs = Faq.objects.get(id=1)
    # context = {'faqs': faqs}
    
    # # print(Faq.question)
    # # print(Faq.answer)
    # return render(request, 'faq.html', context)
    fn = User.first_name
    return render(request,'faq.html',{'fname':fn})
    
    
from django.shortcuts import render
from .models import FAQ

def faq_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})

def submit_question(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            faq = FAQ(question=question)
            faq.save()
            return redirect('faq')
    else:
        form = FAQForm()
    return render(request, 'faq.html', {'form': form})

# FAQ for admin response
def admin_view(request):
    faqs = FAQ.objects.all()
    return render(request, 'admin.html', {'faqs': faqs})

def answer_question(request, pk):
    # faq = get_object_or_404(FAQ, pk=pk)
    # if request.method == 'POST':
    #     form = AnswerForm(request.POST)
    #     if form.is_valid():
    #         answer = form.cleaned_data['answer']
    #         faq.answer = answer
    #         faq.save()
    #         return redirect('admin')
    # else:
    #     form = AnswerForm()
    faq = get_object_or_404(FAQ, pk=pk)
    if request.user.is_superuser or request.user == faq.user:
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.cleaned_
    return render(request, 'admin.html', {'form': form})



def delete_question(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    faq.deleted = True
    faq.save()
    return redirect('admin')

def delete_question(request, pk):
    faq = get_object_or_404(FAQ, pk=pk)
    faq.deleted = True
    faq.save()
    return redirect('admin')


# Patient list


# def doctorPatient(request):
#     # patient_list_instance = PatientList.objects.get(pk=1)
#     # patient_instance = patient_list_instance.patient_profile
#     # patient_name = patient_instance.pat_name
#     # patient_age = patient_instance.pat_age
#     # patients = patient.objects.all()
#     return render(request, 'doctorAcc.html', {'patients': patient.objects.all()})
#     # do something with the patient name and age
