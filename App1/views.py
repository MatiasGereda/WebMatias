from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

def familiar(request):
    Familiar1=Familiar(nombre="Gabriel",edad=28,anio_nacimiento="1994-08-06")
    Familiar1.save()

    return render(request, "hermano.html", {"Familiar1" : Familiar1})

def mascota(request):
    mascota1=Mascota(nombre="Yvri",edad=1,anio_nacimiento="2021-12-9")
    mascota1.save()

    return render(request, "mascota.html", {"mascota1" : mascota1})

def vehiculo(request):
    vehiculo1=Vehiculo(marca="FIAT",modelo="Palio Weeknd",anio= 2006)
    vehiculo1.save()

    return render(request, "vehiculo.html", {"vehiculo1" : vehiculo1})

def agregarVehiculo(request):
    if request.method=="POST":
        modelo=request.POST["modelo"]
        marca=request.POST["marca"]
        anio=request.POST["anio"]
        vehiculo= Vehiculo(marca=marca, modelo=modelo,anio=anio)
        vehiculo.save()
        return render (request, "inicio.html", {"mensaje" : "Vehiculo guardado"})

    else:
        return render (request, "agregarVehiculo.html")

def agregarMascota(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        edad=request.POST["edad"]
        anio_nacimiento=request.POST["anio_nacimiento"]
        mascota= Mascota(nombre=nombre, edad=edad,anio_nacimiento=anio_nacimiento)
        mascota.save()
        return render (request, "inicio.html", {"mensaje" : "Mascota guardada"})

    else:
        return render (request, "agregarMascota.html")

def agregarFamiliar(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        edad=request.POST["edad"]
        anio_nacimiento=request.POST["anio_nacimiento"]
        familiar= Familiar(nombre=nombre, edad=edad, anio_nacimiento=anio_nacimiento)
        familiar.save()
        return render (request, "inicio.html", {"mensaje" : "Familiar guardado"})

    else:
        return render (request, "agregarFamiliar.html")


def busquedaF(request):
    return render (request, "busquedaF.html")

def buscarF(request):
    
    nombre=request.GET["nombre"]
    if nombre!="":
        familiares= Familiar.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadosBusquedaF.html", {"familiares" : familiares})
    else:
        return render(request, "busquedaF.html", {"mensaje" : "ingresar nombre"})

#########################

def busquedaM(request):
    return render (request, "busquedaM.html")

def buscarM(request):
    
    nombre=request.GET["nombre"]
    if nombre!="":
        mascotas= Mascota.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadosBusquedaM.html", {"mascotas" : mascotas})
    else:
        return render(request, "busquedaM.html", {"mensaje" : "ingresar nombre"})

########################

def busquedaV(request):
    return render (request, "busquedaV.html")

def buscarV(request):
    
    marca=request.GET["marca"]
    if marca!="":
        vehiculos= Vehiculo.objects.filter(marca__icontains=marca)
        return render(request, "resultadosBusquedaV.html", {"vehiculos" : vehiculos})
    else:
        return render(request, "busquedaV.html", {"mensaje" : "ingresar marca"})
