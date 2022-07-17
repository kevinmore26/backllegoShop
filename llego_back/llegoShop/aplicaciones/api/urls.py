from importlib.resources import path
from django.urls import path
from .views import ProductoView ,BuscarProducto ,BuscarProductoTipoSubtipo

 
urlpatterns = [
    path('listarProducto/',ProductoView.as_view(),name='productos_list'), 
    path('listarProducto/<int:id>',ProductoView.as_view(),name='productos_proccess'), 
    path('buscarProducto/',BuscarProducto.as_view(),name='productos_proccess'),
    path('buscarProductoTipoSubTipo/',BuscarProductoTipoSubtipo.as_view(),name='productos_proccess'),
    
]
