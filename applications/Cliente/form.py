from django import forms 

from .models import Cliente 

class ClienteForm(forms.ModelForm):
    """Form definition for Cliente."""

    class Meta:
        """Meta definition for Clienteform."""

        model = Cliente
        fields = ('apellidos',
                  'nombres',
                  'nombre_completo',
                  'dni'
                  )#campos para crear a los clientes
        
