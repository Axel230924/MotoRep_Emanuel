from django.contrib import admin

from Apps.Catalogos.Proveedor.models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):

    search_fields = ['Nombre']
    list_display = ['Nombre', 'NumTelefono']
