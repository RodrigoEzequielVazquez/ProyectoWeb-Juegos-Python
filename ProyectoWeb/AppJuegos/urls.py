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
    
    path("about",about,name="about"),
    
    # Juegos PS4
    
    path("verJuegosPS4",verJuegosPS4, name="verJuegosPS4"),
    
    #agregar Juegos con formularios 
    
    path("juegosPS4Formulario",juegosPS4Formulario, name="juegosPS4Formulario"),
       
    path("leerMasPS4/<int:pk>",leerMasPS4, name="leerMasPS4"),
    
    path("actualizarJuegosPS4Formulario/<int:pk>",actualizarJuegosPS4Formulario, name="actualizarJuegosPS4Formulario"),
    
    path("eliminarJuegoPS4/<int:pk>",eliminarJuegoPS4, name="eliminarJuegoPS4"),
    
    # Juegos PS5
    
    path("verJuegosPS5",verJuegosPS5, name="verJuegosPS5"),
    
    path("juegosPS5Formulario",juegosPS5Formulario, name="juegosPS5Formulario"),
    
    path("leerMasPS5/<int:pk>",leerMasPS5, name="leerMasPS5"),
    
    path("actualizarJuegosPS5Formulario/<int:pk>",actualizarJuegosPS5Formulario, name="actualizarJuegosPS5Formulario"),
    
    path("eliminarJuegoPS5/<int:pk>",eliminarJuegoPS5, name="eliminarJuegoPS5"),
    # Estudios
    
    path("listaDeEstudios/",ListaEstudios.as_view(),name="listaDeEstudios"),
    
    path("crearEstudios/",CrearEstudios.as_view(),name="crearEstudios"),
    
    path("actualizarEstudio/<int:pk>",ActualizarEstudio.as_view(),name="actualizarEstudio"),
    
    path("eliminarEstudio/<int:pk>",EliminarEstudio.as_view(),name="eliminarEstudio"),
    
    # Login
    
    path("login",loginRequest,name="login"),
    
    #Registro
    
    path("register",register,name="register"),
    
    # Logout
    
    path("logout",cerrarSesion,name="logout"),
    
    # Editar perfil
    
    path("editarPerfil",editarPerfil,name="editarPerfil"),
    
    path("agregarAvatar",agregarAvatar,name="agregarAvatar")
   
]
