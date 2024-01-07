from django.db import models

# Create your models here.


class Juegos(models.Model):
    
    nombre=models.CharField(max_length=30)
    genero= models.CharField(max_length=30)
    anio= models.IntegerField()
