from django.contrib import admin
from .models import TurnoCaja, MovimientoCaja, DetallePagoMov

@admin.register(TurnoCaja)
class TurnoCajaAdmin(admin.ModelAdmin):
    list_display = ['FechaApertura', 'FechaCierre', 'MontoInicial', 'MontoFinal', 'Egresos', 'DinDigital', 'DinEfectivo', 'EmpleadoId', 'CajaId']
    search_fields = ['EmpleadoId__Nombre', 'CajaId__NumCaja']
    list_filter = ['FechaApertura', 'FechaCierre']

@admin.register(MovimientoCaja)
class MovimientoCajaAdmin(admin.ModelAdmin):
    list_display = ['FechaMovimiento', 'MontoTotal', 'Descripcion', 'TipoMovimientoId', 'TurnoCajaId', 'CompraId', 'CompraCreditoId', 'FacturaId', 'FacturaCreditoId']
    search_fields = ['TipoMovimientoId__Nombre', 'TurnoCajaId__EmpleadoId__Nombre']
    list_filter = ['FechaMovimiento']

@admin.register(DetallePagoMov)
class DetallePagoMovAdmin(admin.ModelAdmin):
    list_display = ['Monto', 'MetodoPagoId', 'MovimientoCajaId']
    search_fields = ['MetodoPagoId__Nombre', 'MovimientoCajaId__TipoMovimientoId__TipoMov']
    list_filter = ['MetodoPagoId']