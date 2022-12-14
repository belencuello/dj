from django import forms 

from .models import Producto 

class ProductoForm(forms.ModelForm):
    """Form definition for Producto."""

    class Meta:
        """Meta definition for Productoform."""

        model = Producto
        fields = ('id',
                  'tipo',
                  'marcaProd',
                  )#campos para crear a los productos