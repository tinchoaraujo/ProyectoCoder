from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppCoder.models import Equipo
# Create your views here.


def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {
        'equipos': equipos,
        'nombre': 'Martín'
    }
    return render(request, 'AppCoder/equipos.html', contexto)


def crear_equipo(request):
    equipo = Equipo(nombre='San Carlos', codigo=2)
    equipo.save()

    return redirect('/app/equipos/')


def show_html(request):
    equipo = Equipo.objects.first()
    contexto = {'equipo': equipo, 'nombre': 'Martín'}
    return render(request, 'index.html', contexto)

