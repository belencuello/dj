from  rest_framework import serializers
from .models import Proveedor

class ProveedorSerializer(serializers.ModelSerializer):
    """Model definition for ProveedorSerializer."""

    # TODO: Define fields here

    class Meta:

       model = Proveedor
       fields = ('__all__')