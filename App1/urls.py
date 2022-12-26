from django.urls import path
from .views import *

urlpatterns = [path("", inicio, name="inicio"),
path("familia/", familiar, name="familiares"),
path("mascota/", mascota, name="mascotas"),
path("vehiculo/", vehiculo, name="vehiculos"),
path("agregarVehiculo/", agregarVehiculo, name="agregarVehiculo"),
path("agregarMascota/", agregarMascota, name="agregarMascota"),
path("agregarFamiliar/", agregarFamiliar, name="agregarFamiliar"),
path("busquedaF/", busquedaF, name="busquedaF"),
path("busquedaV/", busquedaV, name="busquedaV"),
path("busquedaM/", busquedaM, name="busquedaM"),
path("buscarF/", buscarF, name="buscarF"),
path("buscarV/", buscarV, name="buscarV"),
path("buscarM/", buscarM, name="buscarM"),

]