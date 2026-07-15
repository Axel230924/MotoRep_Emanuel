from django.contrib import admin
from .models import Producto
from .models import DetalleProducto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['Nombre', 'Codigo', 'CategoriaId']
    search_fields = ['Nombre', 'Codigo']

@admin.register(DetalleProducto)
class DetalleProductoAdmin(admin.ModelAdmin):
    list_display = ['ProductoId', 'MarcaId', 'MotoId', 'ColorProductoId', 'TamañoProductoId']
    search_fields = ['ProductoId__Nombre', 'MarcaId__Nombre', 'MotoId__Modelo']