from django.contrib import admin

from Apps.Catalogos.CondicionPago.models import CondicionPago

@admin.register(CondicionPago)
class CondicionPagoAdmin(admin.ModelAdmin):

    search_fields = ['Condicion']
    list_display = ['Condicion']
