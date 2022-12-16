from django.contrib import admin
from django.urls import path, re_path, include
from . import views 
app_name = "proveedor_app"

urlpatterns = [
     path(   #estructura path compuesta por tres partes
       'inicial/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
    ),
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
        name='Detalle del proveedor'
    ),
    path(
        'proveedor/create/',
        views.ProveedorCreateView.as_view(),
        name='Alta de Proveedor'
    ),
    path(
        'proveedor/update/<pk>/',
        views.ProveedorUpdateView.as_view(),
        name='Modificar proveedor'
    ),
    path(
        'proveedor/baja/<pk>/',
        views.ProveedorDeleteView.as_view(),
        name='Baja de proveedor'
    ),
        
    path(
        'api/lista/',
        views.ProveedorListApiView.as_view(),
        name='lista-api'
    ),
]
    


