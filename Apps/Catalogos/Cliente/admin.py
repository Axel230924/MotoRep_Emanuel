from django.contrib import admin

from Apps.Catalogos.Cliente.models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):

    search_fields = ['Nombre', 'Apellido']
    list_display = ['Nombre', 'Apellido', 'NumCedula', 'NumTelefono']
