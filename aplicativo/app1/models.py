from django.db import models

# Create your models here.

class Principal(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    ocupacion = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100) 
    documento = models.CharField(max_length=20)

class Secundario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField() #integerfield sirve para poner numeros enteros
    principal = models.OneToOneField(Principal, on_delete= models.CASCADE, null=False, blank=False) #one to one crea relacion uno a uno 