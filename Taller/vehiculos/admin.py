from django.contrib import admin
from .models import Marca, Modelo, Vehiculo

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Vehiculo)