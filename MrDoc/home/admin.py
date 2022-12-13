from django.contrib import admin
from home.models import RegUsers, NearBy_Doctor, Appointment_List, departments, reviewers, rating


# Register your models here.
admin.site.register(RegUsers)
admin.site.register(NearBy_Doctor)
admin.site.register(Appointment_List)
admin.site.register(departments)
admin.site.register(reviewers)
admin.site.register(rating)


