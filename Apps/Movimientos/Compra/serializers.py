from rest_framework.serializers import ModelSerializer, CharField
from .models import Compra, DetalleCompra, CompraCredito
from Apps.Movimientos.Producto.serializers import DetalleProductoSerializer
from .serializers import CompraSerializer
class DetalleCompraSerializer(ModelSerializer):

    DetalleProducto_nombre = DetalleProductoSerializer(read_only=True)
    compra_nombre = CompraSerializer(read_only=True)

    class Meta:
        
        model = DetalleCompra
        fields = [
                    'Cantidad',
                    'PrecioUnitario',
                    'Subtotal',
                    'CompraId',
                    'DetalleProductoId',
                    'DetalleProducto_nombre',
                    'compra_nombre'
                   ]
        
        read_only_fields = [
                                'Subtotal'
                            ]

class CompraSerializer(ModelSerializer):

    Proveedor_nombre = CharField(source='ProveedorId.Nombre', read_only=True)
    CondicionPago_nombre = CharField(source='CondicionPagoId.Condicion', read_only=True)
    detalles_Compra = DetalleCompraSerializer(many=True,)

    class Meta:
        
        model = Compra
        fields = [
                    'FechaCompra',
                    'NumCompra',
                    'Total',
                    'ProveedorId',
                    'CondicionPagoId',
                    'Proveedor_nombre',
                    'CondicionPago_nombre',
                    'detalles_Compra'
                  ]
        
        read_only_fields = [
                                'Total'
                            ]
        
class CompraCreditoSerializer(ModelSerializer):

    Compra_nombre = CompraSerializer(read_only=True)
    class Meta:
        
        model = CompraCredito
        fields = [
                    'Monto',
                    'SaldoPendiente',
                    'FechaInicio',
                    'FechaVencimiento',
                    'CompraId',
                    'Compra_nombre'
                ]
        
        read_only_fields = [
                                'FechaInicio',
                                'SaldoPendiente',
                                'CompraId',
                                'Monto'
                            ]