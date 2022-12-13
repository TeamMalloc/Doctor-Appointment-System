from django.db import models

# Create your models here.

class ThaiFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes
    
class IndianFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes

class DumplingsFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes

class ContinentalFood(models.Model):
    FoodTypes = models.CharField(max_length=50)
    FoodTitle = models.CharField(max_length=100)
    FoodSubTitle = models.CharField(max_length=120)
    FoodPrice = models.IntegerField()
    FoodDesc = models.CharField(max_length=150)
    FoodImage = models.ImageField(upload_to="img/")
    def __str__(self):
        return self.FoodTypes
        
    

    
    

    
