# from django.db import models
from django.db import models



# Create your models here.
class contact(models.Model):
    usename = models.CharField(max_length = 122)
    fname = models.CharField(max_length = 122)
    lname = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    pass1 = models.CharField(max_length = 122)
    pass2 = models.CharField( max_length= 122)
    date = models.DateField()

class doctorAccount(models.Model):
    usename = models.CharField(max_length = 122)
    fname = models.CharField(max_length = 122)
    lname = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    pass1 = models.CharField(max_length = 122)
    pass2 = models.CharField( max_length= 122)
    date = models.DateField()
