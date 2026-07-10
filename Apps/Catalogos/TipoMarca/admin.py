from django.contrib import admin

from Apps.Catalogos.TipoMarca.models import TipoMarca

@admin.register(TipoMarca)
class TipoMarcaAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Tipo']
    list_display = ['id', 'Tipo', 'Estado']
