from django.db import models

# Create your models here.

class Productos (models.Model):
   
    TIPO_PRODUCTO = [ ("1",'comidaRapida'),("2","miniMarket"),("3","supermercado") ] 
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50 )
    descripcion = models.CharField(max_length=200)
    stockProducto = models.CharField(max_length=20)
    productoImagen =  models.CharField(max_length=300)
    precio = models.CharField(max_length=10)
    productoTipo = models.CharField(max_length=10 ,null=False, choices=TIPO_PRODUCTO)
    productoSubTipo = models.CharField(max_length=10)
     


    