from importlib.resources import path
from django.urls import path
from .views import ProductoView,BuscadorProducto

 
urlpatterns = [
    path('listarProducto/',ProductoView.as_view(),name='productos_list'),
    
    path('listarProducto/<int:id>',ProductoView.as_view(),name='productos_proccess'),
    path('buscarProducto/',BuscadorProducto.as_view(),name='productos_filtro') 
]
