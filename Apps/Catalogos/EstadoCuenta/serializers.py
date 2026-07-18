from rest_framework.serializers import ModelSerializer
from .models import EstadoCuenta

class EstadoCuentaSerializers(ModelSerializer):

    class Meta:
        
        model = EstadoCuenta
        fields = ['DescripcionEstado']