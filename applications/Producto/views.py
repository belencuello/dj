from django.shortcuts import render
# Create your views here
from .serializer import ProductoSerializer
from rest_framework.generics import ListAPIView
from django.views.generic import (

    ListView,
    DeleteView,
    CreateView,
    TemplateView,
    UpdateView,
    DetailView,
)
from .models import Producto
from .form import ProductoForm
from django.urls import reverse_lazy

class Inicio(TemplateView):     #Esta vista hereda de TemplateView y solo nos muestra un template
   template_name = "inicio.html"

#CONSULTA QUE Nos devuelve todos los objetos del tipo producto de la BD
class ProductoListView(ListView):#esta vista hace una consulta a la BS y devuelve todos los objetos
    model: Producto
    template_name = "producto/lista.html"
    ordering = "nombre"
    paginate_by: 3
    context_object_name = "productos"
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','') #aca le estoy piediendo que del metodo get me obtenga algo cuyo nombre sea segun parametro que va a ser el nombre del campo() #GET es cuando quiero traer cierta ingo del servidor POST cuando quiero enviar info del servidor
        #lista que muestra
        lista = Producto.objects.filter(
            nombre__icontains = palabra_clave
            )#los objetos del modelo producto los voy a filtar con algun criterio
        return lista

class BuscarProductoListView(ListView):
    model = Producto
    template_name = "producto/buscar.html"
    ordering = "nombre"
    context_object_name = "productos"

#para realizar una consulta segun criterio de busqueda usamos metodo get queryset
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','') #aca le estoy piediendo que del metodo get me obtenga algo cuyo nombre sea segun parametro que va a ser el nombre del campo() #GET es cuando quiero traer cierta ingo del servidor POST cuando quiero enviar info del servidor
    #lista que muestra
        lista = Producto.objects.filter(
            nombre__icontains = palabra_clave
            )#los objetos del modelo producto los voy a filtar con algun criterio
        return lista


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto/detalle.html"
    context_object_name = 'detalle'


class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto/create.html"
    form_class = ProductoForm#asociamos esta vista al formulario
    success_url = reverse_lazy('producto_app:Lista de Productos')
    #redefinimos una funcion form_valid que se va a ejecutar una vez que se determine que el formulario sea valido o sea que todos sus campos esten completados
    def form_valid(self, form):
        prod= form.save(commit=False)#guarda en esta variable pero no en la BD
        prod = prod.tipo + '' + prod.marcaprod#AUTOMATICAMENTE SE GENERA EL NOMBRE COMPLETO EN BASE AL APELLIDO Y NOMBRE QUE INGRESE 
        prod.save()#guarda en la BD
        return super(ProductoCreateView, self).form_valid(form)


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto/update.html"
    form_class = ProductoForm
    success_url = reverse_lazy('producto_app:Lista de Productos')

    def form_valid(self, form):
        emp = form.save()#guarda en esta variable pero no en la BD
        return super(ProductoUpdateView, self).form_valid(form)



class ProductoDeleteView(DeleteView):#se usa para borrar registros
    model = Producto
    template_name = "producto/delete.html"
    success_url = reverse_lazy('producto_app:Lista de Productos')#funcion q dirige la URL a onde se le diga


class ProductoListApiView(ListAPIView):

    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.all()