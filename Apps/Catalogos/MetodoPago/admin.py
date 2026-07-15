from django.contrib import admin

from Apps.Catalogos.MetodoPago.models import MetodoPago

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):

    search_fields = ['Metodo']
    list_display = ['Metodo']
