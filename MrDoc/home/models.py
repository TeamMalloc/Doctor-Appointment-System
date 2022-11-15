from django.db import models

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
    
