from django.contrib import admin
from django.urls import path
from ourRestarant import views

urlpatterns = [
    path("",views.index,name="home"),
    path('thai',views.thai, name='thai'),
    path('indian',views.indian, name='indian'),
    path('dumplings',views.dumplings, name='dumplings'),
    path('continental',views.continental, name='continental'),
]
