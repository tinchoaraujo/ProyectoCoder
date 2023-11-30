from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Equipo
from AppCoder.forms import EquipoForm, BusquedaEquipoForm
# Create your views here.


def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {
        'equipos': equipos,
        'nombre': 'Martín',
        'form': BusquedaEquipoForm(),
    }
    return render(request, 'AppCoder/equipos.html', contexto)


def crear_equipo(request):
    equipo = Equipo(nombre='San Carlos', codigo=2)
    equipo.save()

    return redirect('/app/equipos/')


def crear_equipo_form(request):
    if request.method == 'POST':
        equipo_formulario = EquipoForm(request.POST)
        if equipo_formulario.is_valid():
            informacion = equipo_formulario.cleaned_data
            equipo_crear = Equipo(nombre=informacion['nombre'], codigo=informacion['codigo'])
            equipo_crear.save()
        return redirect('/app/equipos/')

    equipo_formulario = EquipoForm()
    contexto = {
        'form': equipo_formulario
    }
    return render(request, 'AppCoder/crear_equipo.html', contexto)


def busqueda_equipo(request):
    nombre = request.GET['nombre']
    equipos = Equipo.objects.filter(nombre__icontains=nombre)

    contexto = {
        'equipos': equipos,
        'nombre': 'Martín',
        'form': BusquedaEquipoForm(),
    }
    return render(request, 'AppCoder/equipos.html', contexto)


def show_html(request):
    equipo = Equipo.objects.first()
    contexto = {'equipo': equipo, 'nombre': 'Martín'}
    return render(request, 'index.html', contexto)


