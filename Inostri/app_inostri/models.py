from django.db import models

# Create your models here.

class Vino(models.Model):
    nombre = models.CharField(max_length=64)
    bodega = models.CharField(max_length=64)
    varietal = models.CharField(max_length=64)
    cosecha = models.IntegerField()
    region = models.CharField(max_length=64)
    provincia = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.nombre} | {self.bodega} | {self.varietal} | {self.region}'

class Bodega(models.Model):
    nombre = models.CharField(max_length=64)
    direccion = models.CharField(max_length=256)
    region = models.CharField(max_length=64)
    provincia = models.CharField(max_length=64)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'{self.nombre} | {self.provincia}'
    
class Varietal(models.Model):
    nombre = models.CharField(max_length=64)
    tipo = models.CharField(max_length=20)
    descripcion = models.TextField

    def __str__(self):
        return f'{self.nombre} | {self.descripcion}'