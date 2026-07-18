from rest_framework.serializers import ModelSerializer
from .models import Empleado

class EmpleadoSerializers(ModelSerializer):
    class Meta:
        model = Empleado
        fields = [
                    'Nombre', 
                    'Apellido',
                    'NumCedula',
                    'NumTelefono',
                    'Direccion'
                  ]
        
        extra_kwargs = {
                            'NumCedula': {'write_only': True},
                            'NumTelefono': {'write_only': True},
                            'Direccion': {'write_only': True}
                       }