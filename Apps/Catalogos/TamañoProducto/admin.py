from django.contrib import admin

from Apps.Catalogos.TamañoProducto.models import TamañoProducto

@admin.register(TamañoProducto)
class TamañoProductoAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Tamaño']
    list_display = ['id', 'Tamaño', 'Estado']