from django.contrib import admin

from Apps.Catalogos.MetodoPago.models import MetodoPago

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Metodo']
    list_display = ['id', 'Metodo', 'Estado']
