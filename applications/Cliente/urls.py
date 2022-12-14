from django.contrib import admin
from django.urls import path, re_path, include
from . import views
app_name = "cliente_app"

urlpatterns = [
    path(   #estructura path compuesta por tres partes
       'inicial/',   #asi termina la url (url/lista)
       views.Inicio.as_view(), #esta es la vista que acabamos de crear en views.py	
       name='Pagina inicial'   #nombre de la url
    ),
    path(
        'cliente/lista/',
        views.ClienteListView.as_view(),
        name='Lista de Clientes'
    ),
    
    path(
        'cliente/buscar/',
        views.BuscarClienteListView.as_view(),
        name='Buscar Clientes'
    ),
   

    path(
        'cliente/detalle/<pk>/',   #<pk>/ se usa para decirle que registro voy a eliminar es el id del cliente
        views.ClienteDetailView.as_view(),
        name='Detalle del cliente'
    ),

    path(
        'cliente/create/',
        views.ClienteCreateView.as_view(),
        name='Alta de Clientes'
    ),

    path(
        'cliente/update/<pk>/',
        views.ClienteUpdateView.as_view(),
        name='Modificar cliente'
    ),
    path(
        'cliente/baja/<pk>/',
        views.ClienteDeleteView.as_view(),
        name='Baja de cliente'
    ),
    path(
        'api/lista/',
        views.ClienteListApiView.as_view(),
        name='lista-api'
    ),
]