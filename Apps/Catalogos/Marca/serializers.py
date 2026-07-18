from rest_framework.serializers import ModelSerializer, CharField
from .models import Marca

class MarcaSerializers(ModelSerializer):
    TipoMarca_nombre = CharField(source='TipoMarcaId.Nombre', read_only=True)

    class Meta:
        model = Marca
        fields = [
                    'Nombre',
                    'TipoMarcaId',
                    'TipoMarca_nombre'
                  ]