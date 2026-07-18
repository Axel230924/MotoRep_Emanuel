from rest_framework.serializers import ModelSerializer
from .models import MetodoPago

class MetodooPagoSerializers(ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ['Metodo']