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
    
    def get (self,request):
        productos = list(Productos.objects.values())
        
        if len(productos)>0:
            datos={'message':"todo salió bien",'productos': productos}

        else:
            datos={'message':"No se encontraron productos"}
            
        return JsonResponse(datos)
    
    def post(self,request):
        
        jd = json.loads(request.body)
        
        Productos.objects.create(nombre=jd['nombre'],descripcion=jd['descripcion'],stockProducto=jd['stockProducto'],productoImagen=jd['productoImagen'])
        datos = {'message':"Success"}
        return JsonResponse(datos)
    
