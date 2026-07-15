from django.contrib import admin
from .models import Compra
from .models import DetalleCompra
from .models import CompraCredito

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['FechaCompra', 'NumCompra', 'Total', 'ProveedorId', 'CondicionPagoId']
    search_fields = ['NumCompra', 'ProveedorId__Nombre']

@admin.register(DetalleCompra)
class DetalleCompraAdmin(admin.ModelAdmin):
    list_display = ['Cantidad', 'PrecioUnitario', 'Subtotal', 'CompraId', 'DetalleProductoId']
    search_fields = ['CompraId__NumCompra', 'DetalleProductoId__Nombre']

@admin.register(CompraCredito)
class CompraCreditoAdmin(admin.ModelAdmin):
    list_display = ['Monto', 'SaldoPendiente', 'FechaInicio', 'FechaVencimiento', 'CompraId']
    search_fields = ['CompraId__NumCompra']