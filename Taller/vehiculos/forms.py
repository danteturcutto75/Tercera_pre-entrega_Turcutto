from django import forms
from .models import Vehiculo

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['marca', 'modelo', 'anio', 'dominio']


class BusquedaForm(forms.Form):
    busqueda = forms.CharField(max_length=10)