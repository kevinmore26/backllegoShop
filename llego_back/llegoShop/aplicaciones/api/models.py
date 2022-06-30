from django.db import models

# Create your models here.

class Productos (models.Model):
    TIPO_PRODUCTO = [(1, 'embutidos'), (2, 'a'), (3, 'b')]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50 )
    descripcion = models.CharField(max_length=200)
    stockProducto = models.CharField(max_length=20)
    productoImagen =  models.CharField(max_length=300)
    precio = models.CharField(max_length=10)
    clienteTipo = models.CharField(choices=TIPO_PRODUCTO,null=False,max_length=10,default='1')


    