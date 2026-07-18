from rest_framework.serializers import ModelSerializer
from .models import Proveedor

class ProveedorSerializers(ModelSerializer):

    class Meta:

        model = Proveedor
        fields = [
                    'Nombre',
                    'NumTelefono',
                  ]
        
        extra_kwargs = {
                            'NumTelefono': {'write_only': True},
                       }        