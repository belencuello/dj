from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListAPIView 
from .serializer import ClienteSerializer
from django.views.generic import (
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView
)

from .models import Cliente
from .form import ClienteForm
from django.urls import reverse_lazy



#CONSULTA QUE Nos devuelve todos los objetos del tipo clientes de la BD
class ClienteListView(ListView):#esta vista hace una consulta a la BS y devuelve todos los objetos
    model: Cliente
    template_name = "cliente/lista.html"
    ordering = "apellidos"
    paginate_by: 3
    context_object_name = "clientes"
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','') #aca le estoy piediendo que del metodo get me obtenga algo cuyo nombre sea segun parametro que va a ser el nombre del campo() #GET es cuando quiero traer cierta ingo del servidor POST cuando quiero enviar info del servidor
        #lista que muestra
        lista = Cliente.objects.filter(
            apellidos__icontains = palabra_clave
            )#los objetos del modelo producto los voy a filtar con algun criterio
        return lista

"""class BuscarClienteListView(ListView):
    model = Cliente
    template_name = "cliente/buscar.html"
    ordering = "apellidos"
    context_object_name = "clientes"

#para realizar una consulta segun criterio de busqueda usamos metodo get queryset
    def get_queryset(self):
      palabra_clave = self.request.GET.get('kword','') #aca le estoy piediendo que del metodo get me obtenga algo cuyo nombre sea segun parametro que va a ser el nombre del campo() #GET es cuando quiero traer cierta ingo del servidor POST cuando quiero enviar info del servidor
    #lista que muestra
      lista = Cliente.objects.filter(
        apellidos__icontains = palabra_clave
        )#los objetos del modelo cliente los voy a filtar con algun criterio
      return lista"""


class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente/detalle.html"
    context_object_name = 'detalle'


class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cliente/create.html"
    form_class = ClienteForm#asociamos esta vista al formulario
    success_url = reverse_lazy('cliente_app:Lista de Clientes')
    #redefinimos una funcion formvari que se va a ejecutar una vez que se determine que el formulario sea valido o sea que todos sus campos esten completados
    def form_valid(self, form):
        emp = form.save(commit=False)#guarda en esta variable pero no en la BD
        emp.nombre_completo = emp.nombres + '' + emp.apellidos#AUTOMATICAMENTE SE GENERA EL NOMBRE COMPLETO EN BASE AL APELLIDO Y NOMBRE QUE INGRESE 
        emp.save()#guarda en la BD
        return super(ClienteCreateView, self).form_valid(form)


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "cliente/update.html"
    form_class = ClienteForm
    success_url = reverse_lazy('cliente_app:Lista de Clientes')

    def form_valid(self, form):
        emp = form.save(commit=False)#guarda en esta variable pero no en la BD
        emp.nombre_completo = emp.nombres + '' + emp.apellidos#AUTOMATICAMENTE SE GENERA EL NOMBRE COMPLETO EN BASE AL APELLIDO Y NOMBRE QUE INGRESE 
        emp.save()#guarda en la BD
        return super(ClienteUpdateView, self).form_valid(form)



class ClienteDeleteView(DeleteView):#se usa para borrar registros
    model = Cliente
    template_name = "cliente/delete.html"
    context_object_name= 'delete'
    success_url = reverse_lazy('cliente_app:Lista de Clientes')#funcion q dirige la URL a onde se le diga

class ClienteListApiView(ListAPIView):

    serializer_class = ClienteSerializer

    def get_queryset(self):
        return Cliente.objects.all()