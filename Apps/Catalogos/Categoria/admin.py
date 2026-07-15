from django.contrib import admin

from Apps.Catalogos.Categoria.models import Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    search_fields = ['Nombre']
    list_display = ['Nombre']
