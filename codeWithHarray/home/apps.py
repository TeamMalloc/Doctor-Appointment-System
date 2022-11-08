from django.apps import AppConfig
from home.models import doctorAccount

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
