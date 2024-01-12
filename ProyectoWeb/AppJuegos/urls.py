"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from AppJuegos.views import *

urlpatterns = [
    path("",inicio, name="Inicio"),
    
    # Juegos PS4
    
    path("verJuegosPS4",verJuegosPS4, name="verJuegosPS4"),
    
    path("agregarJuegosPS4",agregarJuegoPS4, name="agregarJuegosPS4"),
    
    path("juegosPS4Formulario",juegosPS4Formulario, name="juegosPS4Formulario"),
    
    path("busquedaJuegosPS4",busquedaJuegosPS4, name="busquedaJuegosPS4"),
    
    path("buscarPS4/",buscarPS4),
    
    # Juegos PS5
    
    path("verJuegosPS5",verJuegosPS5, name="verJuegosPS5"),
    
    path("agregarJuegosPS5",agregarJuegoPS5, name="agregarJuegosPS5"),
    
    path("juegosPS5Formulario",juegosPS5Formulario, name="juegosPS5Formulario"),
    
    path("busquedaJuegosPS5",busquedaJuegosPS5, name="busquedaJuegosPS5"),
    
    path("buscarPS5/",buscarPS5),
    
    # Estudios
    
    path("agregarEstudios",agregarEstudios, name="agregarEstudios"),
    
    path("verEstudios",verEstudios, name="verEstudios"),
    
    path("estudiosFormulario",estudiosFormulario, name="estudiosFormulario"),
   
]
