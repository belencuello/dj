from django import forms 

from .models import Proveedor 

class ProveedorForm(forms.ModelForm):
    """Form definition for Proveedor."""

    class Meta:
        """Meta definition for Proveedorform."""

        model = Proveedor
        fields = ('id',
                  'nombre',
                  'rubro',
                  )#campos para crear a 