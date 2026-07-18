from rest_framework.serializers import ModelSerializer, CharField
from .models import Moto

class MotoSerializers(ModelSerializer):

    Marca_nombre = CharField(source='MarcaId.Nombre', read_only=True)

    class Meta:

        model = Moto
        fields = [
                    'Modelo',
                    'Año',
                    'MarcaId',
                    'Marca_nombre'
                  ]