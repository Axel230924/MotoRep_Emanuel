from rest_framework.serializers import ModelSerializer
from .models import Categoria

class CategoriaSerializers(ModelSerializer):
    
    class Meta:

        model = Categoria
        fields = ['Nombre']