from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from AppCoder.models import Equipo
from AppCoder.forms import EquipoForm, BusquedaEquipoForm
# Create your views here.


class EquipoList(ListView):
    model = Equipo
    template_name = 'AppCoder/equipos_1.html'


class EquipoDetalle(DetailView):
    model = Equipo
    template_name = 'AppCoder/equipo_detalle.html'


class EquipoCreacion(CreateView):
    model = Equipo
    success_url = '/app/equipos/listar'
    template_name = 'AppCoder/crear_equipo.html'
    fields = ['nombre', 'fundado']


class EquipoActualizacion(UpdateView):
    model = Equipo
    success_url = '/app/equipos/listar'
    template_name = 'AppCoder/crear_equipo.html'
    fields = ['nombre', 'fundado']


class EquipoEliminar(DeleteView):
    model = Equipo
    template_name = 'AppCoder/eliminar_equipo.html'
    success_url = '/app/equipos/listar'


def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {
        'equipos': equipos,
        'nombre': 'Martín',
        'form': BusquedaEquipoForm(),
    }
    return render(request, 'AppCoder/equipos.html', contexto)


def crear_equipo(request):
    equipo = Equipo(nombre='Club Nacional de Football', fundado=1899)
    equipo.save()

    return redirect('/app/equipos/')


def crear_equipo_form(request):
    if request.method == 'POST':
        equipo_formulario = EquipoForm(request.POST)
        if equipo_formulario.is_valid():
            informacion = equipo_formulario.cleaned_data
            equipo_crear = Equipo(nombre=informacion['nombre'], fundado=informacion['fundado'])
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


