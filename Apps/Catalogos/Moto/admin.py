from django.contrib import admin
from .models import Moto

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    search_fields = ['id', 'Modelo']
    list_display = ['id', 'Modelo', 'Año', 'MarcaId']