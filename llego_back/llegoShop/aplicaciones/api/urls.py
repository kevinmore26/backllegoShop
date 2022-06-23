from importlib.resources import path
from django.urls import path
from .views import ProductoView

 
urlpatterns = [
    path('listarProducto/',ProductoView.as_view(),name='productos_list')
     
]
