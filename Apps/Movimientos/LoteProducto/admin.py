from django.contrib import admin
from .models import LoteProducto

@admin.register (LoteProducto)

class LoteProductoAdmin (admin.ModelAdmin):
    list_field = ['Cantidad', 'PrecioUnitario', 'PrecioVenta', 'FechaRegistro', 'DetalleCompraId']
    search_field =['FechaRegistro', 'DetalleCompraId__DetalleProductoId__ProductoId__Nombre']