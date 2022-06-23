from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Productos
import json

# Create your views here.

class ProductoView(View):
    
    def get (self,request):
        productos = list(Productos.objects.values())
        
        if len(productos)>0:
            datos={'message':"todo salió bien",'productos': productos}

        else:
            datos={'message':"No se encontraron productos"}
            
        return JsonResponse(datos)
    
    
