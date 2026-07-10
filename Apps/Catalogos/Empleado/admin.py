from django.contrib import admin

from Apps.Catalogos.Empleado.models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Nombre']
    list_display = ['id', 'Nombre', 'Apellido', 'NumCedula', 'NumTelefono', 'Direccion', 'Estado']
