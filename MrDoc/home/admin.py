from django.contrib import admin
from home.models import RegUsers, NearBy_Doctor, Appointment_List, departments
from home.models import FAQ
from home.models import patient


# Register your models here.
admin.site.register(RegUsers)
admin.site.register(NearBy_Doctor)
admin.site.register(Appointment_List)
admin.site.register(departments)
admin.site.register(FAQ)
admin.site.register(patient)



