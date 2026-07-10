from django.contrib import admin

from Apps.Catalogos.CondicionPago.models import CondicionPago

@admin.register(CondicionPago)
class CondicionPagoAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Condicion']
    list_display = ['id', 'Condicion', 'Estado']
