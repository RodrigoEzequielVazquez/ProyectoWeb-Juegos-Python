from django import forms

class JuegosPS4Formulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    anio= forms.IntegerField()
    
class JuegosPS5Formulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    anio= forms.IntegerField()
    
class EstudiosFormulario(forms.Form):
    
    nombre=forms.CharField(max_length=30)
    lanzamientosFamosos=forms.CharField(max_length=30)