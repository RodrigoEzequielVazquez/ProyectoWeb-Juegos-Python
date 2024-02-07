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
from django.shortcuts import redirect
import datetime



# Create your views here.

#Inicio

def inicio(request):
    # Obtener todos los juegos de PS4
    juegos_ps4 = JuegosPS4.objects.all()

    # Obtener el último juego de PS4 de toda la colección
    ultimo_juego_ps4 = juegos_ps4.last() if juegos_ps4 else None

    # Obtener todos los juegos de PS5
    juegos_ps5 = JuegosPS5.objects.all()

    # Obtener el último juego de PS5 de toda la colección
    ultimo_juego_ps5 = juegos_ps5.last() if juegos_ps5 else None

    # Pasar los juegos a la plantilla
    contexto = {
        'ultimo_juego_ps4': ultimo_juego_ps4,
        'ultimo_juego_ps5': ultimo_juego_ps5,
    }
    
    return render(request, "AppJuegos/inicio.html", {"user": request.user, "contexto": contexto})


#Registro

def register(request):
    
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = RegistrarUsuario(request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            form.save()
            return redirect("/")
        
    else:
        # form = UserCreationForm()
        form = RegistrarUsuario(request.POST)
        
    return render(request,"AppJuegos/registro.html", {"form":form})  

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
                
                return redirect("/")
        
    else:
            
        form = AuthenticationForm()
    
    return render(request,"AppJuegos/login.html", {"form":form})

#Logout

def cerrarSesion(request):
    logout(request)
     
    return redirect("/")

#Editar Perfil

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

#Vista para subir imagenes(avatares)

from django.shortcuts import redirect

def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.usuario = request.user  # Asigna directamente el usuario actual
            avatar.save()
            return redirect("/")
    else:
        form = AvatarFormulario()
        # Excluimos el campo de usuario del formulario
        form.fields['usuario'].widget = forms.HiddenInput()
    return render(request, "AppJuegos/agregarAvatar.html", {"form": form})


# about

def about(request):
    
    return render(request,"AppJuegos/about.html")
    
# CRUD Juegos PS4

def verJuegosPS4(request):
    
    juegosPS4 = JuegosPS4.objects.all() #obtengo todos los datos en mi tabla Juegos
     
    info = {"juegos":juegosPS4}
        
    return render(request,"AppJuegos/verJuegosPS4.html",info) 

# Funcion de agregar juegos de PS4 con formularios.

def juegosPS4Formulario(request):
    
    if request.method == "POST":
        
        juego = JuegosPS4(nombre= request.POST["nombre"],genero= request.POST["genero"], año= request.POST["año"], descripcion= request.POST["descripcion"],fecha= request.POST["fecha"], imagen= request.FILES["imagen"])
        
        juego.save()
        
        return redirect("/verJuegosPS4")
    
    else:
        
        form = JuegosPS4Formulario()
    
    return render(request,"AppJuegos/juegosPS4Formulario.html",{"form":form})

def actualizarJuegosPS4Formulario(request, pk):
    juegoElegido = JuegosPS4.objects.get(id=pk)
    
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
            return redirect("/verJuegosPS4")
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

def eliminarJuegoPS4(request, pk):
    
    juegoElegido = JuegosPS4.objects.get(id=pk)
    
    juegoElegido.delete()
    
    juegos = JuegosPS4.objects.all()
    
    contexto= {"juegos":juegos, "user":request.user}
    
    return render(request,"AppJuegos/verJuegosPS4.html",contexto)

#Leer mas sobre el juego

def leerMasPS4(request, pk):
    
    juegoElegido = JuegosPS4.objects.get(id=pk)
    
    return render(request,"AppJuegos/leerMasPS4.html",{"juego":juegoElegido})
        
# agregar y ver los juegos de PS5

def verJuegosPS5(request):
    
    juegosPS5 = JuegosPS5.objects.all() #obtengo todos los datos en mi tabla Juegos
    
    info = {"juegos":juegosPS5}
     
    return render(request,"AppJuegos/verJuegosPS5.html",info) 

# Funcion de agregar juegos de PS5 con formularios.

def juegosPS5Formulario(request):
    
    if request.method == "POST":
        
        juego = JuegosPS5(nombre= request.POST["nombre"],genero= request.POST["genero"], año= request.POST["año"], descripcion= request.POST["descripcion"],fecha= request.POST["fecha"], imagen= request.FILES["imagen"])
        
        juego.save()
        
        return redirect("/verJuegosPS5")
    
    else:
        
        form = JuegosPS5Formulario()
    
    return render(request,"AppJuegos/juegosPS5Formulario.html",{"form":form})

def actualizarJuegosPS5Formulario(request, pk):
    juegoElegido = JuegosPS5.objects.get(id=pk)
    
    if request.method == "POST":
        form = JuegosPS5Formulario(request.POST, request.FILES)  # Incluir request.FILES aquí
        if form.is_valid():
            info = form.cleaned_data
            juegoElegido.nombre = info["nombre"]
            juegoElegido.genero = info["genero"]
            juegoElegido.año = info["año"]
            juegoElegido.descripcion = info["descripcion"]
            juegoElegido.imagen = info["imagen"]
            juegoElegido.fecha = info["fecha"]
            juegoElegido.save()
            return redirect("/verJuegosPS5")
    else:
        initial_data = {
            "nombre": juegoElegido.nombre,
            "genero": juegoElegido.genero,
            "año": juegoElegido.año,
            "descripcion": juegoElegido.descripcion,
            "imagen": juegoElegido.imagen,
            "fecha": datetime.date.today()
        }
        form = JuegosPS5Formulario(initial=initial_data)
    
    return render(request, "AppJuegos/actualizarJuegosPS5Formulario.html", {"form": form})

def eliminarJuegoPS5(request, pk):
    
    juegoElegido = JuegosPS5.objects.get(id=pk)
    
    juegoElegido.delete()
    
    juegos = JuegosPS5.objects.all()
    
    contexto= {"juegos":juegos}
    
    return render(request,"AppJuegos/verJuegosPS5.html",contexto)

#Leer mas sobre el juego

def leerMasPS5(request, pk):
    
    juegoElegido = JuegosPS5.objects.get(id=pk)
    
    return render(request,"AppJuegos/leerMasPS5.html",{"juego":juegoElegido})

# CRUD de estudios
    
class ListaEstudios(ListView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/estudiosList.html"
    
class CrearEstudios(CreateView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/crearEstudios.html" 
    fields = ["nombre","lanzamientosFamosos"]
    success_url = "/listaDeEstudios"
    
class ActualizarEstudio(UpdateView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/actualizarEstudio.html" 
    fields = ["nombre","lanzamientosFamosos"]
    success_url = "/listaDeEstudios"    
   
class EliminarEstudio(DeleteView):
    
    model = EstudiosDeJuegos
    template_name = "AppJuegos/eliminarEstudio.html" 
    success_url = "/listaDeEstudios"   

