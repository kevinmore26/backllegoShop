from django.db import models

# Create your models here.

class Productos (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    stockProducto = models.PositiveIntegerField(max_length=4)
    productoImage =  models.CharField(max_length=300)