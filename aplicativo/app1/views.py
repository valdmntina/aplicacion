from django.shortcuts import render
from django.http import HttpResponse
from.models import Principal, Secundario

# Create your views here.

def index(request):
    #obtiene todos los elementos de principal
    principales = Principal.objects.all()
    return render(request, 'index.html', {
        'principales': principales
        })

def storage(request, nombre, apellido, edad, ocupacion, correo, documento):
    principalito = Principal(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        ocupacion=ocupacion,
        correo=correo,
        documento=documento
        )
    principalito.save()
    return HttpResponse('guarde principalito')

def storage2(request, nombre, apellido, edad, principal_id):
    secundarito = Secundario(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        principal_id=principal_id
    )
    secundarito.save()
    return HttpResponse('guarde secundarito')