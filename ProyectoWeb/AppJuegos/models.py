from django.db import models
from django.contrib.auth.models import User

# Create your models here.

 
class JuegosPS4(models.Model):
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
    nombre=models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="imagenesPS4", null=True, blank=True)
    año= models.IntegerField()
    fecha= models.DateField(auto_now=True)

class JuegosPS5(models.Model):
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
    nombre=models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    anio= models.IntegerField()
    
class EstudiosDeJuegos(models.Model):
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
    nombre=models.CharField(max_length=30)
    lanzamientosFamosos=models.CharField(max_length=30)
    
class AvatarImagen(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    
    def __str__(self):
        return f"{self.usuario} - {self.imagen}"
    
