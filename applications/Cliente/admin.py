from django.contrib import admin
from.models import Cliente
# Register you models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'apellidos',
        'nombres',
        'nombre_completo',
        'dni',
    ]
    search_fields = ['apellidos',]
    list_filter = ['nombres', 'dni']

admin.site.register(Cliente, ClienteAdmin)