from django.urls import path
from . import views

urlpatterns = [
    path('agregar_vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('editar/<int:vehiculo_id>/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar/<int:vehiculo_id>/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('listar_modelos/', views.listar_modelos, name='listar_modelos'),
    path('lista_vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('', views.lista_vehiculos, name='lista_vehiculos'),
]