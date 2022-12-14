from django.contrib import admin
from django.urls import path, re_path, include
from . import views
app_name = "producto_app"

urlpatterns = [
    path(
        'producto/',
        views.Producto.as_view(),
        name='Pagina producto'
    ),
    path(
        'producto/lista/',
        views.ProductoListView.as_view(),
        name='Lista de Productos'
    ),
    path(
        'producto/buscar/',
        views.BuscarProductoListView.as_view(),
        name='Buscar Productos'
    ),
    path(
        'producto/detalle/<pk>/',#<pk>/ se usa para decirle que registro voy a eliminar es el id del cliente
        views.ProductoDetailView.as_view(),
        name='Detalle del Producto'
    ),
    path(
        'producto/create/',
        views.ProductoCreateView.as_view(),
        name='Alta de Producto'
    ),
    path(
        'producto/update/<pk>/',
        views.ProductoUpdateView.as_view(),
        name='Modificar Producto'
    ),
   path(
        'api/lista/',
        views.ProductoListApiView.as_view(),
        name='lista-api'
    ),
]


