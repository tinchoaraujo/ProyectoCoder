"""
URL configuration for ProyectoCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder.views import crear_equipo, show_html, mostrar_equipos, crear_equipo_form, busqueda_equipo, EquipoList, \
    EquipoDetalle, EquipoCreacion, EquipoActualizacion, EquipoEliminar

urlpatterns = [
    path('show/', show_html),
    path('agregar_equipo/', crear_equipo),
    path('equipos/', mostrar_equipos),
    path('equipos/listar', EquipoList.as_view(), name='EquipoList'),
    path('equipo/<int:pk>', EquipoDetalle.as_view(), name='EquipoDetail'),
    path('buscar/', busqueda_equipo),
    path('equipo/', crear_equipo_form),
    path('crear_equipo', EquipoCreacion.as_view(), name='EquipoCreate'),
    path('editar/<int:pk>', EquipoActualizacion.as_view(), name='EquipoEditar'),
    path('eliminar/<int:pk>', EquipoEliminar.as_view(), name='EquipoEliminar'),
]
