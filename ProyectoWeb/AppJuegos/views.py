from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    
    return render(request,"AppJuegos/inicio.html")

# agregar y ver los juegos de PS4

def agregarJuegoPS4(request):
    
    juego1= JuegosPS4(nombre="Resident Evil 4",genero="Accion-aventura",anio=2005)
    juego1.save()
    
    return HttpResponse("Se agrego un juego")
    
def verJuegosPS4(request):
    
    juegosPS4 = JuegosPS4.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":juegosPS4}
        
    return render(request,"AppJuegos/verJuegosPS4.html",info) 

# agregar y ver los juegos de PS5

def agregarJuegoPS5(request):
    
    juego1= JuegosPS5(nombre="Spider-Man 2",genero="Acción-aventura",anio=2023)
    juego1.save()
    
    return HttpResponse("Se agrego un juego")
    
def verJuegosPS5(request):
    
    juegosPS5 = JuegosPS5.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":juegosPS5}
        
    return render(request,"AppJuegos/verJuegosPS5.html",info) 

# agregar y ver los estudios

def agregarEstudios(request):
    
    estudio1= EstudiosDeJuegos(nombre="Bend Studio",lanzamientosFamosos="Days gone")
    estudio1.save()
    
    return HttpResponse("Se agrego un nuevo estudio")
    
def verEstudios(request):
    
    estudios = EstudiosDeJuegos.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"estudios":estudios}
        
    return render(request,"AppJuegos/verEstudios.html",info) 


# Funciones de agregar juegos de PS4 con formularios.

def juegosPS4Formulario(request):
    
    if request.method == "POST":
        
        juego = JuegosPS4(nombre= request.POST["nombre"],genero= request.POST["genero"], anio= request.POST["anio"])
        
        juego.save()
        
        return render(request,"AppJuegos/inicio.html")
    
    else:
        
        miFormulario = JuegosPS4Formulario()
    
    return render(request,"AppJuegos/juegosPS4Formulario.html",{"miFormulario":miFormulario})

def busquedaJuegosPS4(request):
    return render(request,"AppJuegos/busquedaJuegosPS4.html")

def buscarPS4(request):
    
    if request.GET["nombre"]:
        
        juego = request.GET["nombre"]
        juegosPS4 = JuegosPS4.objects.filter(nombre__icontains=juego)
        
        return render(request,"AppJuegos/resultadosBusquedaJuegosPS4.html",{"juegos":juegosPS4,"nombre":juego})
        
    else:
        
       respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)


# Funciones de agregar juegos de PS5 con formularios.

def juegosPS5Formulario(request):
    
    if request.method == "POST":
        
        juego = JuegosPS5(nombre= request.POST["nombre"],genero= request.POST["genero"], anio= request.POST["anio"])
        
        juego.save()
        
        return render(request,"AppJuegos/inicio.html")
    
    else:
        
        miFormulario = JuegosPS5Formulario()
    
    return render(request,"AppJuegos/juegosPS5Formulario.html",{"miFormulario":miFormulario})

def busquedaJuegosPS5(request):
    return render(request,"AppJuegos/busquedaJuegosPS5.html")

def buscarPS5(request):
    
    if request.GET["nombre"]:
        
        juego = request.GET["nombre"]
        juegosPS4 = JuegosPS5.objects.filter(nombre__icontains=juego)
        
        return render(request,"AppJuegos/resultadosBusquedaJuegosPS5.html",{"juegos":juegosPS4,"nombre":juego})
        
    else:
        
       respuesta = "No enviaste datos"
    
    return HttpResponse(respuesta)


# funciones para agregar estudios por formularios

def estudiosFormulario(request):
    
    if request.method == "POST":
        
        estudios = EstudiosDeJuegos(nombre= request.POST["nombre"],lanzamientosFamosos= request.POST["lanzamientosFamosos"])
        
        estudios.save()
        
        return render(request,"AppJuegos/inicio.html")
    
    else:
        
        miFormulario = EstudiosFormulario()
    
    return render(request,"AppJuegos/estudiosFormulario.html",{"miFormulario":miFormulario})