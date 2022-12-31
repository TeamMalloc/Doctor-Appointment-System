from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name="Home"),
    path('registration',views.registration,name="reg"),
    path('userRole', views.userRole,name="userRole"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('doctorRole',views.doctorRole,name="doctorRole"),
    path('patientRole',views.patientRole,name="patientRole"),
]
