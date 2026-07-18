from rest_framework.serializers import ModelSerializer
from .models import TipoMovCaja

class TipoMovCajaSerializers(ModelSerializer):

    class Meta:

        model = TipoMovCaja
        fields = ['TipoMov']
        