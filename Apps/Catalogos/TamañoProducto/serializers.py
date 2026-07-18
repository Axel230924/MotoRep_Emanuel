from rest_framework.serializers import ModelSerializer
from .models import TamañoProducto

class TamañoProductoSerializers(ModelSerializer):

    class Meta:

        model = TamañoProducto
        fields = ['Tamaño']