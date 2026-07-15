from django.contrib import admin

from Apps.Catalogos.Empleado.models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    search_fields = ['Nombre', 'Apellido']
    list_display = ['Nombre', 'Apellido', 'NumCedula', 'NumTelefono', 'Direccion']
