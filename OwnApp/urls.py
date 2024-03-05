from django.urls import path
from OwnApp.views import *

urlpatterns = [
    path("crear_producto/", crear_producto, name='c_producto'),
    path("crear_usuario/", crear_usuario, name='c_usuario'),
    path("crear_req/", crear_requerimiento,name='c_req'),
    path("busqueda/", busqueda,name='busc'),
    path("", inicio, name='Home'),
]