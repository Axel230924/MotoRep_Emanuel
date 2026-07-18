from rest_framework.serializers import ModelSerializer, CharField
from .models import Producto, LoteProducto
from Apps.Movimientos.Compra.serializers import DetalleCompraSerializer

class LoteProductoSerializer(ModelSerializer):

    DetalleCompra_nombre = DetalleCompraSerializer(read_only=True)

    class Meta:
        
        model = LoteProducto
        fields = [
                    'PrecioVenta',
                    'Cantidad',
                    'PrecioUnitario',
                    'FechaRegistro',
                    'DetalleCompraId',
                    'DetalleCompra_nombre'
                  ]

        read_only_fields = ['FechaRegistro', 'PrecioUnitario', 'DetalleCompraId']