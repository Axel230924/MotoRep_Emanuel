from django.contrib import admin

from Apps.Catalogos.TipoMovCaja.models import TipoMovCaja

@admin.register(TipoMovCaja)
class TipoMovCajaAdmin(admin.ModelAdmin):

    search_fields = ['id', 'TipoMov']
    list_display = ['id', 'TipoMov', 'Estado']
