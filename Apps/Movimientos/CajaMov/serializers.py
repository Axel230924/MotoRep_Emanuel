from rest_framework.serializers import ModelSerializer, CharField
from .models import TurnoCaja, MovimientoCaja, DetallePagoMov
from Apps.Catalogos.Empleado.serializers import EmpleadoSerializer
from Apps.Movimientos.Factura.serializers import FacturaSerializer, FacturaCreditoSerializer
from Apps.Movimientos.Compra.serializers import CompraSerializer, CompraCreditoSerializer
from Apps.Movimientos.CajaMov.serializers import TurnoCajaSerializer

class DetallePagoMovSerializer(ModelSerializer):

    class Meta:
        model = DetallePagoMov
        fields = [
                    'Monto',
                    'MetodoPagoId',
                    'MovimientoCajaId'
        ]

        read_only_fields = ['MovimientoCajaId']

class MovimientoCajaSerializer(ModelSerializer):

    TipoMovCaja_nombre = CharField(source='TipoMovCajaId.TipoMov', read_only=True)
    Compra_nombre = CompraSerializer(read_only=True)
    CompraCredito_nombre = CompraCreditoSerializer(read_only=True)
    Factura_nombre = FacturaSerializer(read_only=True)
    FacturaCredito_nombre = FacturaCreditoSerializer(read_only=True)
    TurnoCaja_nombre = TurnoCajaSerializer(read_only=True)
    detalles_PagoMov = DetallePagoMovSerializer(many=True)

    class Meta:
        
        model = MovimientoCaja
        fields = [
                    'FechaMovimiento',
                    'MontoTotal',
                    'Descripcion',
                    'TipoMovCajaId',
                    'TurnoCajaId',
                    'CompraId',
                    'CompraCreditoId',
                    'FacturaId',
                    'FacturaCreditoId',
                    'TipoMovCaja_nombre',
                    'Compra_nombre',
                    'CompraCredito_nombre',
                    'Factura_nombre',
                    'FacturaCredito_nombre',
                    'TurnoCaja_nombre',
                    'detalles_PagoMov'
                  ]
        
        read_only_fields = [
                                'FechaMovimiento',
                                'MontoTotal',
                                'TurnoCajaId',
                                'CompraId',
                                'CompraCreditoId',
                                'FacturaId',
                                'FacturaCreditoId'
                            ]

class TurnoCajaSerializer(ModelSerializer):

    Empleado_nombre = EmpleadoSerializer(read_only=True)
    Caja_nombre = CharField(source='CajaId.NumCaja', read_only=True)
    detalles_MovimientoCaja = MovimientoCajaSerializer(many=True)

    class Meta:
        
        model = TurnoCaja
        fields = [
                    'FechaApertura',
                    'FechaCierre',
                    'MontoInicial',
                    'MontoFinal',
                    'Egresos',
                    'DinDigital',
                    'DinEfectivo',
                    'EmpleadoId',
                    'CajaId',
                    'Empleado_nombre',
                    'Caja_nombre',
                    'detalles_MovimientoCaja'
                  ]
        
        read_only_fields = [
                                'FechaApertura',
                                'EmpleadoId',
                                'CajaId',
                                'MontoFinal',
                                'Egresos',
                                'DinDigital',
                                'DinEfectivo'
                            ]