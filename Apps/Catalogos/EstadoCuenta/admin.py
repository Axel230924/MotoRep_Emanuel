from django.contrib import admin

from Apps.Catalogos.EstadoCuenta.models import EstadoCuenta

@admin.register(EstadoCuenta)
class EstadoCuentaAdmin(admin.ModelAdmin):

    search_fields = ['id', 'DescripcionEstado']
    list_display = ['id', 'DescripcionEstado', 'Estado']
