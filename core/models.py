from django.db import models

# Create your models here.
class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=99)

class Fabricante(models.Models):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=99)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=99)
    Fabricante = models.ForeignKey(Fabricante, null='', blank='', on_delete=models.CASCADE)
    Componente = models.ForeignKey(Componente, null='', blank='', on_delete=models.CASCADE)
    Precio = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)
    Imagen = models.ImageField(upload_to='static/img/productos/')
    
   