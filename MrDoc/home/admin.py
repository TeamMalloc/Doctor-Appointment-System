from django.contrib import admin
from home.models import RegUsers, NearBy_Doctor, Appointment_List, departments,patient,health


# Register your models here.
admin.site.register(RegUsers)
admin.site.register(NearBy_Doctor)
admin.site.register(Appointment_List)
admin.site.register(departments)
admin.site.register(patient)
admin.site.register(health)






