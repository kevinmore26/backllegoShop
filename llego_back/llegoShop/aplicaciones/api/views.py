from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Productos
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator 
import json
 
# Create your views here.

class ProductoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request , *args , **kwargs )  :
        return super().dispatch(request, *args, **kwargs)
    
 
    
    def get (self,request, id = 0 ):
        
        if (id>0):
            productos=list(Productos.objects.filter(id=id).values())
            if len(productos) >0:
                producto = productos[0]
                datos = {'message':"Todo bien",'productos':producto}
            
            else:
                datos = {'message:"Producto no encontrado'}
            
            return JsonResponse(datos)
             
        
        else: 
            productos = list(Productos.objects.values())
        
            if len(productos)>0:
                datos={'message':"todo salió bien",'productos': productos}

            else:
                datos={'message':"No se encontraron productos"}
            
            return JsonResponse(datos)
    
    
    
    
    def post(self,request,nombre=''):
        
                jd = json.loads(request.body)
            
             
                Productos.objects.create(nombre=jd['nombre'],descripcion=jd['descripcion'],stockProducto=jd['stockProducto'],productoImagen=jd['productoImagen'],precio=jd['precio'],productoTipo=jd['productoTipo'])
                datos = {'message':"Success"}
                return JsonResponse(datos)
    

    def put(self,request,id=0):
        
        
            jd= json.loads(request.body)
            productos = list(Productos.objects.filter(id=id).values())
            if len(productos) > 0:
                productos= Productos.objects.get(id=id)
                productos.nombre = jd['nombre']
                productos.descripcion = jd['descripcion']
                productos.stockProducto = jd['stockProducto']
                productos.productoImagen = jd['productoImagen']
                productos.precio = jd['precio']
                productos.productoTipo = jd['productoTipo']
                productos.save()
                datos = {'message':"Todo bien"}
            else:
                datos = {'message':"no se encontró el producto"}
            
            return JsonResponse(datos)
    
    
    def delete(self,request,id=0):
        
        productos = list(Productos.objects.filter(id=id).values())
        if len(productos)>0:
            Productos.objects.filter(id=id).delete()
            datos = {'message':"Eliminado exitosamente"}
        else :
            datos = {'message': "Producto no encontrado"}
        
        return JsonResponse(datos)
    

class BuscarProducto(View):
    queryset =  list(Productos.objects.all().values())
    def get( self , request):
        nombre = request.GET.get('nombre')
        print(nombre)   
        
        productoEncontrado = None
        if nombre :
            if productoEncontrado is not None:
                productoEncontrado = productoEncontrado.filter(nombre__icontains = nombre).all()
                datos = {'message':"todo mal"}
            
            else : 
                productoEncontrado = list(Productos.objects.filter(
                    nombre__icontains = nombre ).all().values()),
                
                datos = { 'message' : "todo bien", 'datos':productoEncontrado}
            
            return JsonResponse(datos)

class BuscarProductoTipo(View):
    queryset =  list(Productos.objects.all().values())
    def get( self , request):
        productoTipo = request.GET.get('productoTipo')
        print(productoTipo)   
        
        productoEncontrado = None
        if productoTipo :
            if productoEncontrado is not None:
                productoEncontrado = productoEncontrado.filter(productoTipo__icontains = productoTipo).all()
                datos = {'message':"todo mal"}
            
            else : 
                productoEncontrado = list(Productos.objects.filter(
                    productoTipo__icontains = productoTipo ).all().values()),
                
                datos = { 'message' : "todo bien", 'datos':productoEncontrado}
            
            return JsonResponse(datos)
        