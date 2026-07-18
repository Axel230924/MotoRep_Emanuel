from rest_framework.serializers import ModelSerializer, CharField
from .models import Factura, DetalleFactura, FacturaCredito
from Apps.Catalogos.Cliente.serializers import ClienteSerializer
from Apps.Movimientos.Factura.serializers import FacturaSerializer
from Apps.Movimientos.LoteProducto.serializers import LoteProductoSerializer

class DetalleFacturaSerializer(ModelSerializer):

    Factura_nombre = FacturaSerializer(read_only=True)
    LoteProducto_nombre = LoteProductoSerializer(read_only=True)

    class Meta:
        
        model = DetalleFactura
        fields = [
                    'Cantidad',
                    'PrecioUnitario',
                    'Subtotal',
                    'FacturaId',
                    'LoteProductoId',
                    'Factura_nombre',
                    'LoteProducto_nombre'
                   ]
        
        read_only_fields = [
                                'Subtotal', 
                                'PrecioUnitario', 
                                'FacturaId'
                            ]

class FacturaSerializer(ModelSerializer):

    Cliente_nombre = ClienteSerializer(read_only=True)
    CondicionPago_nombre = CharField(source='CondicionPagoId.Condicion', read_only=True)
    detallesFactura = DetalleFacturaSerializer(many=True)

    class Meta:
        
        model = Factura
        fields = [
                    'NumFactura',
                    'Fecha',
                    'Total',
                    'ClienteId',
                    'CondicionPagoId',
                    'Cliente_nombre',
                    'CondicionPago_nombre',
                    'detallesFactura'
                  ]
        
        read_only_fields = [
                                'Total',
                                'NumFactura',
                                'Fecha'
                            ]

class FacturaCreditoSerializer(ModelSerializer):

    Factura_nombre = FacturaSerializer(read_only=True)
    EstadoCuenta_nombre = CharField(source='EstadoCuentaId.DescripcionEstado', read_only=True)

    class Meta:
        
        model = FacturaCredito
        fields = [
                    'FechaInicio',
                    'FechaVencimiento',
                    'MontoTotal',
                    'SaldoPendiente',
                    'FacturaId',
                    'EstadoCuentaId',
                    'Factura_nombre',
                    'EstadoCuenta_nombre'
                ]
        
        read_only_fields = [
                                'FechaInicio',
                                'MontoTotal',
                                'SaldoPendiente',
                                'FacturaId'
                            ]
