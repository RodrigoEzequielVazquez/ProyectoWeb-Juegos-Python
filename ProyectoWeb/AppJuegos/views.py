from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView , DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime



# Create your views here.

def inicio(request):
    
    return render(request,"AppJuegos/inicio.html")


#Vista para subir imagenes(avatares)

@login_required()
def agregarAvatar(request):
   
    if request.method == "POST":
        
        form = AvatarFormulario(request.POST, request.FILES)
        
        if form.is_valid():
            
            informacion = form.cleaned_data
            
            avatar = AvatarImagen(usuario=request.user, imagen=informacion["imagen"])
            
            avatar.save()
            
            return render(request,"AppJuegos/inicio.html",{"form":form})
    
    else:
        
        form = AvatarFormulario()
        
    return render(request,"AppJuegos/agregarAvatar.html",{"form":form})

# about

def about(request):
    
    return render(request,"AppJuegos/about.html")
    
# agregar y ver los juegos de PS4

def agregarJuegoPS4(request):
    
    juego1= JuegosPS4(nombre="Resident Evil 4",genero="Accion-aventura",descripcion="Es un juego de zombies",imagen="",fecha=None,año=2005)
    juego1.save()
    
    return HttpResponse("Se agrego un juego")

@login_required  
def verJuegosPS4(request):
    
    juegosPS4 = JuegosPS4.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":juegosPS4}
        
    return render(request,"AppJuegos/verJuegosPS4.html",info) 

# Funciones de agregar juegos de PS4 con formularios.

def juegosPS4Formulario(request):
    
    if request.method == "POST":
        
        juego = JuegosPS4(nombre= request.POST["nombre"],genero= request.POST["genero"], año= request.POST["año"], descripcion= request.POST["descripcion"],fecha= request.POST["fecha"], imagen= request.FILES["imagen"])
        
        juego.save()
        
        return render(request,"AppJuegos/inicio.html")
    
    else:
        
        form = JuegosPS4Formulario()
    
    return render(request,"AppJuegos/juegosPS4Formulario.html",{"form":form})

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

def actualizarJuegosPS4Formulario(request, juegoNombre):
    juegoElegido = JuegosPS4.objects.get(nombre=juegoNombre)
    
    if request.method == "POST":
        form = JuegosPS4Formulario(request.POST, request.FILES)  # Incluir request.FILES aquí
        if form.is_valid():
            info = form.cleaned_data
            juegoElegido.nombre = info["nombre"]
            juegoElegido.genero = info["genero"]
            juegoElegido.año = info["año"]
            juegoElegido.descripcion = info["descripcion"]
            juegoElegido.imagen = info["imagen"]
            juegoElegido.fecha = info["fecha"]
            juegoElegido.save()
            return render(request, "AppJuegos/inicio.html")
    else:
        initial_data = {
            "nombre": juegoElegido.nombre,
            "genero": juegoElegido.genero,
            "año": juegoElegido.año,
            "descripcion": juegoElegido.descripcion,
            "imagen": juegoElegido.imagen,
            "fecha": datetime.date.today()
        }
        form = JuegosPS4Formulario(initial=initial_data)
    
    return render(request, "AppJuegos/actualizarJuegosPS4Formulario.html", {"form": form})

def eliminarJuegoPS4(request, juegoNombre):
    
    juegoElegido = JuegosPS4.objects.get(nombre=juegoNombre)
    
    juegoElegido.delete()
    
    juegos = JuegosPS4.objects.all()
    
    contexto= {"juegos":juegos}
    
    return render(request,"AppJuegos/verJuegosPS4.html",contexto)

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

# Funciones de agregar juegos de PS5 con formularios.

def juegosPS5Formulario(request):
    
    if request.method == "POST":
        
        juego = JuegosPS5(nombre= request.POST["nombre"],genero= request.POST["genero"], anio= request.POST["anio"])
        
        juego.save()
        
        return render(request,"AppJuegos/inicio.html")
    
    else:
        
        form = JuegosPS5Formulario()
    
    return render(request,"AppJuegos/juegosPS5Formulario.html",{"form":form})

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
        
        form = EstudiosFormulario()
    
    return render(request,"AppJuegos/estudiosFormulario.html",{"form":form})

class ListaEstudios(LoginRequiredMixin,ListView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/estudiosList.html"
    
class CrearEstudios(CreateView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/crearEstudios.html" 
    fields = ["nombre","lanzamientosFamosos"]
    success_url = "/AppJuegos/listaDeEstudios"
    
class ActualizarEstudio(UpdateView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/crearEstudios.html" 
    fields = ["nombre","lanzamientosFamosos"]
    success_url = "/AppJuegos/listaDeEstudios"    
   
class EliminarEstudio(DeleteView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/eliminarEstudio.html" 
    success_url = "/AppJuegos/listaDeEstudios"   

#Login

def loginRequest(request):
    
    if request.method == "POST":
        
        form = AuthenticationForm(request,data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contraseña = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password=contraseña)
            
            if user is not None:
                login(request, user)
                
                return render(request,"AppJuegos/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        
    else:
            
        form = AuthenticationForm()
    
    return render(request,"AppJuegos/login.html", {"form":form})


def register(request):
    
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = RegistrarUsuario(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"AppJuegos/inicio.html", {"mensaje":"Usuario Creado"})
        
    else:
        # form = UserCreationForm()
        form = RegistrarUsuario(request.POST)
        
    return render(request,"AppJuegos/registro.html", {"form":form})  

@login_required
def cerrarSesion(request):
    logout(request)
     
    return render(request,"AppJuegos/logout.html")

def editarPerfil(request):
    
    usuarioActual = request.user
    
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = RegistrarUsuario(request.POST)
        
        if form.is_valid():
            
            info = form.cleaned_data
            
            usuarioActual.first_name = info["first_name"]
            usuarioActual.last_name = info["last_name"]
            usuarioActual.email = info["email"]
            usuarioActual.set_password(info["password1"])
            
            usuarioActual.save()
            return render(request,"AppJuegos/inicio.html", {"mensaje":"Usuario actualizado"})
        
    else:
        # form = UserCreationForm()
        form = EditarUsuario(initial={"first_name": usuarioActual.first_name,"last_name": usuarioActual.last_name,"email": usuarioActual.email})
        
    return render(request,"AppJuegos/editarUsuario.html", {"form":form})  

