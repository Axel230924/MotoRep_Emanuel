from django.contrib import admin

from Apps.Catalogos.Categoria.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    search_fields = ['id', 'Nombre']
    list_display = ['id', 'Nombre', 'Estado']
