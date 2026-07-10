from django.contrib import admin

from Apps.Catalogos.ColorProducto.models import ColorProducto

@admin.register(ColorProducto)
class ColorProductoAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Color']
    list_display = ['id', 'Color', 'Estado']
