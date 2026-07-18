from rest_framework.serializers import ModelSerializer
from .models import ColorProducto

class ColorProductoSerializers(ModelSerializer):

    class Meta:
        
        model = ColorProducto
        fields = ['Color']