from django.shortcuts import render,HttpResponse
from ourRestarant.models import ThaiFood,IndianFood,DumplingsFood,ContinentalFood
from django.core.files import File

# Create your views here.
def index(request):
    
    return render(request,'Yummy/index.html',)
    #return HttpResponse("this is home page r")

def thai(request):
    TypeFood1 = "Appetizers"
    TypesFood = "Salads"
    TypesFood2 = "Soups"
    objThaiFood = ThaiFood.objects.all()
    return render(request,'Yummy/thai.html',{"tf":objThaiFood,"sa":TypesFood,"ap":TypeFood1,"so":TypesFood2})

def indian(request):
    return render(request,'Yummy/indian.html')

def dumplings(request):
    return render(request,'Yummy/dumplings.html')

def continental(request):
    return render(request,'Yummy/continental.html')

