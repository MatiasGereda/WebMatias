from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre =models.CharField(max_length=50)
    edad=models.IntegerField()
    anio_nacimiento= models.DateField()

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    anio= models.IntegerField()

class Mascota(models.Model):
    nombre =models.CharField(max_length=50)
    edad=models.IntegerField()
    anio_nacimiento= models.DateField()


