from django.shortcuts import render, get_object_or_404, redirect
from .models import Marca, Modelo, Vehiculo
from .forms import VehiculoForm, BusquedaForm 
from django.http import JsonResponse
from django.db.models import Q

def agregar_vehiculo(request):
    
    marcas = Marca.objects.all()
    modelos = Modelo.objects.none()

    if 'marca' in request.GET:
        marca_id = request.GET.get('marca')
        modelos = Modelo.objects.filter(marca_id=marca_id)

    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')    
        else:
            return render(request, 'agregar_vehiculo.html', {'form': form, 'marcas': marcas, 'modelos': modelos, 'error': "No se pudo agregar el vehículo, revise los datos"})      
    else:
        form = VehiculoForm()

    return render(request, 'agregar_vehiculo.html', {'form': form, 'marcas': marcas, 'modelos': modelos})


def editar_vehiculo(request, vehiculo_id):
    marcas = Marca.objects.all()
    modelos = Modelo.objects.none()
    if 'marca' in request.GET:
            marca_id = request.GET.get('marca')
            modelos = Modelo.objects.filter(marca_id=marca_id)
    
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
        else:
            return render(request, 'editar_vehiculo.html', {'form': form, 'marcas': marcas, 'modelos': modelos, 'error': "No se pudo editar el vehículo, revise los datos"})
    else:
        form = VehiculoForm(instance=vehiculo)   
    
    return render(request, 'editar_vehiculo.html', {'form': form, 'marcas': marcas, 'modelos': modelos})

def listar_modelos(request):
    marca_id = request.GET.get('marca_id')
    modelos = Modelo.objects.filter(marca_id=marca_id).values('id', 'nombre')
    return JsonResponse({'modelos': list(modelos)})

def eliminar_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_vehiculos')
    return render(request, 'eliminar_vehiculo.html', {'vehiculo': vehiculo})

def buscar_vehiculo(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            busqueda = form.cleaned_data['busqueda']
            resultados = Vehiculo.objects.filter(dominio=busqueda)
            resultados = Vehiculo.objects.filter(
                Q(dominio__icontains=busqueda) |  
                Q(marca__nombre__icontains=busqueda) |  
                Q(modelo__nombre__icontains=busqueda)
            )
            return render(request, 'resultados_busqueda.html', {'resultados': resultados})
    else:
        form = BusquedaForm()
    return render(request, 'buscar_vehiculo.html', {'form': form})

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})
