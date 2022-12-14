from  rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """Model definition for ProductoSerializer."""

    # TODO: Define fields here

    class Meta:

       model = Producto
       fields = ('__all__')