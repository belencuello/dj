from  rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    """Model definition for ClienteSerializer."""

    # TODO: Define fields here

    class Meta:

       model = Cliente
       fields = ('__all__')


