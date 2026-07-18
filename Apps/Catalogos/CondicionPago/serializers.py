from rest_framework.serializers import ModelSerializer
from .models import CondicionPago

class CondicionPagoSerializers(ModelSerializer):

    class Meta:
        
        model = CondicionPago
        fields = ['Condicion']