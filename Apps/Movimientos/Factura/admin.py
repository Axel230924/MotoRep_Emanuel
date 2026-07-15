from django.contrib import admin
from .models import Factura
from .models import FacturaCredito
from .models import DetalleFactura

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ['Fecha', 'NumFactura', 'Total', 'CondicionPagoId', 'ClienteId']
    search_fields = ['NumFactura', 'ClienteId__Nombre']

@admin.register(FacturaCredito)
class FacturaCredito(admin.ModelAdmin):
    list_display = ['FechaInicio', 'FechaVencimiento', 'MontoTotal', 'SaldoPendiente', 'FacturaId', 'EstadoCuentaId']
    search_fields = ['FechaInicio', 'FacturaId__NumFactura']

@admin.register(DetalleFactura)
class DetalleFacturaAdmin(admin.ModelAdmin):
    list_display = ['Cantidad', 'PrecioUnitario', 'Subtotal', 'FacturaId', 'LoteProductoId']
    search_fields = ['FacturaId__NumFactura']
    