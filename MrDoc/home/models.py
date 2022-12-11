from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegUsers(models.Model):
    UserName = models.CharField(max_length = 122)
    Fname = models.CharField(max_length = 122)
    Lname = models.CharField(max_length = 122)
    Email = models.EmailField(max_length=254)
    Password = models.IntegerField()
    CPassword = models.IntegerField()
    Date = models.DateField()

    def __str__(self):
        return self.UserName

class NearBy_Doctor(models.Model):
    doctor_name = models.CharField(max_length=122)
    department = models.CharField(max_length=122)
    location = models.CharField(max_length=122)
    working_H = models.CharField(max_length=122)
    
    def __str__(self):
        return self.doctor_name

# for book appointment
class Appointment_List(models.Model):
    se_dept = models.CharField(max_length=122)
    se_doc = models.CharField(max_length=122)
    patient_name = models.CharField(max_length=122)
    patient_phone = models.IntegerField()
    patient_email = models.EmailField(max_length=254)
    calendar = models.DateField()

    def __str__(self):
        return self.patient_name

#For departments
class departments(models.Model):
    dep_name = models.CharField(max_length=50)
    def __str__(self):
        return self.dep_name

# Doctor account:
class doctorAccount(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    depName = models.CharField(max_length=100)
    Clinic = models.CharField(max_length=120)
    Degree = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    charge = models.IntegerField()
    langauge = models.CharField(max_length=100)
    def __str__(self):
        return self.name

# Review section:
class review(models.Model):
    name = models.CharField(max_length=50)
    reviews = models.CharField(max_length=200)
    time = models.TimeField()
    

    

    
