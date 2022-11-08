from multiprocessing import context
from tkinter import Variable
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import contact
from home.models import doctorAccount

# Create your views here.
def index(request):
    context={
        'variable':'i am hello'
    }
    # return HttpResponse('this is homepage')
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

    # return HttpResponse('this is about page')

def services(request):
    return render(request,'services.html')

    # return HttpResponse('this is services page')

def contact(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        con = contact(usename=uname,fname=fname,lname=lname,email=email,pass1=pass1,pass2=pass2)
        con.save()
    # return HttpResponse('this is a contact page')
    return render(request,'contact.html')

def docAcc(request):
    return render(request,'docAcc.html')

def patiAcc(request):
    return render(request,'patiAcc.html')


def doctorAccount(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        con = doctorAccount(usename=uname,fname=fname,lname=lname,email=email,pass1=pass1,pass2=pass2)
        con.save()
    # return HttpResponse('this is a contact page')
    return render(request,'contact.html')


