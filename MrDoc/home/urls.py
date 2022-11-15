

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('contact',views.contact,name = 'contact'),
    path('about',views.about,name = 'about'),
    path('services',views.services,name = 'services'),
    path('signUp',views.signUp,name = 'signUp'),
    path('login',views.login,name = 'login'),
    path('signout',views.signout,name = 'signout'),
    path('base',views.base,name = 'base'),
    path('doctorAcc',views.doctorAcc,name = 'doctorAcc'),
    path('NearByDoc',views.NearByDoc,name = 'NearByDoc'),
    path('emDoc',views.emDoc,name = 'emDoc'),

]


