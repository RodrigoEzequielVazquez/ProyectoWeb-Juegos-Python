from django.shortcuts import render
from django.http import HttpResponse
from .models import Juegos

# Create your views here.

def agregarJuego(request):
    
    juego1= Juegos(nombre="Resident Evil 4",genero="Accion-aventura",anio=2005)
    juego1.save()
    
    return HttpResponse("Se agrego un juego")
    
def verJuego(request):
    
    misJuegos = Juegos.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":misJuegos}
        
    return render(request,"juegos.html",info) 
