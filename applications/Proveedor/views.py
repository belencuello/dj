from django.shortcuts import render
# Create your views here.

from rest_framework.generics import ListAPIView 
#from .serializer import ProveedorSerializer

from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)

from .models import Proveedor
from .form import ProveedorForm
from django.urls import reverse_lazy




#CONSULTA QUE Nos devuelve todos los objetos del tipo clientes de la BD
class ProveedorListView(ListView):#esta vista hace una consulta a la BS y devuelve todos los objetos
    model: Proveedor
    template_name = "proveedor/lista.html"
    ordering = "nombre"
    paginate_by: 3
    context_object_name = "proveedores"
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','') #aca le estoy piediendo que del metodo get me obtenga algo cuyo nombre sea segun parametro que va a ser el nombre del campo() #GET es cuando quiero traer cierta ingo del servidor POST cuando quiero enviar info del servidor
        #lista que muestra
        lista = Proveedor.objects.filter(
            nombre__icontains = palabra_clave
            )#los objetos del modelo producto los voy a filtar con algun criterio
        return lista

class BuscarProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/buscar.html"
    ordering = "nombre"
    context_object_name = "proveedores"

#para realizar una consulta segun criterio de busqueda usamos metodo get queryset
def get_queryset(self):
    palabra_clave = self.request.GET.get('kword','') #aca le estoy piediendo que del metodo get me obtenga algo cuyo nombre sea segun parametro que va a ser el nombre del campo() #GET es cuando quiero traer cierta ingo del servidor POST cuando quiero enviar info del servidor
    #lista que muestra
    lista = Proveedor.objects.filter(
        nombre__icontains = palabra_clave
    )#los objetos del modelo cliente los voy a filtar con algun criterio
    return lista


class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor/detalle.html"
    context_object_name = 'detalle'


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = "proveedor/create.html"
    form_class = ProveedorForm#asociamos esta vista al formulario
    success_url = reverse_lazy('proveedor_app:Lista de Proveedores')
    #redefinimos una funcion formvari que se va a ejecutar una vez que se determine que el formulario sea valido o sea que todos sus campos esten completados
    def form_valid(self, form):
        emp = form.save(commit=False)#guarda en esta variable pero no en la BD
        emp.save()#guarda en la BD
        return super(ProveedorCreateView, self).form_valid(form)


class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proveedor/update.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('proveedor_app:Lista de Proveedores')

    def form_valid(self, form):
        emp = form.save(commit=False)#guarda en esta variable pero no en la BD
        emp.save()#guarda en la BD
        return super(ProveedorUpdateView, self).form_valid(form)



class ProveedorDeleteView(DeleteView):#se usa para borrar registros
    model = Proveedor
    template_name = "proveedor/delete.html"
    success_url = reverse_lazy('proveedor_app:Lista de Proveedores')#funcion q dirige la URL a onde se le diga


class ProveedorListApiView(ListAPIView):

   # serializer_class = ProveedorSerializer


    def get_queryset(self):
        return Proveedor.objects.all()