from django.db import models
from categorias.models import Categoria
import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# models.py

def get_image_path(instance, filename):
    producto_id = instance.producto.id
    numero_imagenes = instance.producto.imagenes.count() + 1
    return os.path.join('media', str(producto_id), f'{producto_id}-img{numero_imagenes}.jpg')

class ImagenProducto(models.Model):
    producto = models.ForeignKey('Producto', on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to=get_image_path, null=True, blank=True)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    short_desc = models.TextField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categorias = models.ManyToManyField(Categoria, related_name='productos')

    def __str__(self):
        return self.nombre
