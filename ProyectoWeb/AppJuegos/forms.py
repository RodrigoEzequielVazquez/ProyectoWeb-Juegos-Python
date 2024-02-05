from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import AvatarImagen


class JuegosPS4Formulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    descripcion = forms.CharField()
    imagen = forms.ImageField()
    año= forms.IntegerField()
    fecha= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
class JuegosPS5Formulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    anio= forms.IntegerField()
    
class EstudiosFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    lanzamientosFamosos=forms.CharField(max_length=30)
    
class RegistrarUsuario(UserCreationForm):
    
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        
        model = User
        fields = ["username", "email", "password1", "password2","first_name", "last_name"]
        
        helps_texts = {k:"" for k in fields}
    

class EditarUsuario(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña",widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    
    class Meta:
        
        model = User
        fields = ["email", "password1", "password2","first_name", "last_name"]
        
        helps_texts = {k:"" for k in fields}
        

class AvatarFormulario(forms.ModelForm):
    
    class Meta:
        
        model = AvatarImagen
        fields = ["usuario","imagen"]
    