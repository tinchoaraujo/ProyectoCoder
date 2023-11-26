from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Equipo
# Create your views here.

def crear_equipo(request):
    equipo = Equipo(nombre='Atenas', codigo=1)
    equipo.save()
    contexto = {'equipo': equipo}

    return render(request, 'index.html', contexto)


def show_html(request):
    equipo = Equipo.objects.first()
    contexto = {'equipo': equipo, 'nombre': 'Martín'}
    return render(request, 'index.html', contexto)