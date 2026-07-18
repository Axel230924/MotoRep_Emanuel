from rest_framework.serializers import ModelSerializer
from .models import TipoMarca

class TipoMarcaSerializers(ModelSerializer):

    class Meta:

        model = TipoMarca
        fields = ['Tipo']