from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(request):
    
    return render(request,"AppJuegos/inicio.html")

def agregarJuegoPS4(request):
    
    juego1= JuegosPS4(nombre="Resident Evil 4",genero="Accion-aventura",anio=2005)
    juego1.save()
    
    return HttpResponse("Se agrego un juego")
    
def verJuegosPS4(request):
    
    juegosPS4 = JuegosPS4.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":juegosPS4}
        
    return render(request,"AppJuegos/verJuegosPS4.html",info) 

def agregarJuegoPS5(request):
    
    juego1= JuegosPS5(nombre="Spider-Man 2",genero="Acción-aventura",anio=2023)
    juego1.save()
    
    return HttpResponse("Se agrego un juego")
    
def verJuegosPS5(request):
    
    juegosPS5 = JuegosPS5.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":juegosPS5}
        
    return render(request,"AppJuegos/verJuegosPS5.html",info) 
