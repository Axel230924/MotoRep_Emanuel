from django.contrib import admin

from Apps.Catalogos.TipoMarca.models import TipoMarca

@admin.register(TipoMarca)
class TipoMarcaAdmin(admin.ModelAdmin):

    search_fields = ['Tipo']
    list_display = ['Tipo']
