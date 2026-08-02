from django.contrib import admin
from .models import Service, Customer, Appointment

admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Appointment)