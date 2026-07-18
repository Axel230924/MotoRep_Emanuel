from rest_framework.serializers import ModelSerializer
from .models import Cliente

class ClienteSerializers(ModelSerializer):

    class Meta:

        model = Cliente
        fields = [
                    'Nombre',
                    'Apellido', 
                    'NumCedula', 
                    'NumTelefono'
                ]
        
        #Campos que no puede visualizar pero si enviar información.
        extra_kwargs =  {
                            'NumCedula': {'write_only': True},
                            'NumTelefono': {'write_only': True}
                        }