from django.contrib import admin
from django.urls import path, re_path, include
from . import views 
app_name = "proveedores_app"

urlpatterns = [
    path(
        'proveedor/lista/',
        views.ProveedorListView.as_view(),
        name='Lista de Proveedores'
    ),
    path(
        'proveedor/buscar/',
        views.BuscarProveedorListView.as_view(),
        name='Buscar Proveedores'
    ),
    path(
        'proveedor/detalle/<pk>/',#<pk>/ se usa para decirle que registro voy a eliminar es el id del cliente
        views.ProveedorDetailView.as_view(),
        name='Detalle del Proveedor'
    ),
    path(
        'proveedor/create/',
        views.ProveedorCreateView.as_view(),
        name='Alta de Proveedor'
    ),
    path(
        'proveedor/update/<pk>/',
        views.ProveedorUpdateView.as_view(),
        name='Modificar Proveedor'
    ),
        
    path(
        'api/lista/',
        views.ProveedorListApiView.as_view(),
        name='lista-api'
    ),
]
    


