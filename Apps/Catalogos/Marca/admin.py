from django.contrib import admin
from Apps.Catalogos.Marca.models import Marca

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    search_fields = ['Nombre']
    list_display = ['Nombre']
