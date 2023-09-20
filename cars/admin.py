# cars/admin.py
from django.contrib import admin
from .models import Maker, Car

admin.site.register(Maker)
admin.site.register(Car)
