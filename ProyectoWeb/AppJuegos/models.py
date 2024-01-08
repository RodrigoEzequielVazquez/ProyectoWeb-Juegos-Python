from django.db import models

# Create your models here.

 
class JuegosPS4(models.Model):
    
    nombre=models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    anio= models.IntegerField()

class JuegosPS5(models.Model):
    
    nombre=models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    anio= models.IntegerField()
    
class EstudiosDeJuegos(models.Model):
    
    nombre=models.CharField(max_length=30)
    lanzamientosFamosos=models.CharField(max_length=30)
    

    
