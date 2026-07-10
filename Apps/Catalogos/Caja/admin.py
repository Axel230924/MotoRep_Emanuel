from django.contrib import admin

from Apps.Catalogos.Caja.models import Caja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):

    search_fields = ['id', 'NumCaja']
    list_display = ['id', 'NumCaja', 'Estado']
