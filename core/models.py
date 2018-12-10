from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Lista(models.Model):
    nombre = models.CharField(max_length=25)
    cant_productos = models.IntegerField()
    total_presupuestado = models.IntegerField()
    total_real = models.IntegerField()
    
    def __str__(self):
        return self.nombre


class Estado_Lista(models.Model):
    nombre = models.CharField(max_length=25)
        
    def __str__(self):
        return self.nombre


class Estado_tienda(models.Model):
    nombre = models.CharField(max_length=25)
        
    def __str__(self):
        return self.nombre



class Region(models.Model):
    nombre = models.CharField(max_length=25)
        
    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=25)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.nombre


class Tienda(models.Model):
    nombre = models.CharField(max_length=25)
    nombre_sucursal = models.CharField(max_length=25)
    direccion = models.CharField(max_length=25)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    website = models.CharField(max_length=50)
    id_estado = models.ForeignKey(Estado_tienda, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class Producto(models.Model):
    nombre = models.CharField(max_length=25)
       
    def __str__(self):
        return self.nombre


class Detalle_Producto(models.Model):
    id_tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    nota_adicional = models.CharField(max_length=250)
    costo_real = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_valorizacion =models.DateField(auto_now=False, auto_now_add=False)


class Detalle_Lista(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    costo_presupuestado = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return self.id_producto