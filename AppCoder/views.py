from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Equipo
# Create your views here.

def crear_equipo(request):
    equipo = Equipo(nombre='Atenas', codigo=1)
    equipo.save()

    return HttpResponse(equipo.nombre)

