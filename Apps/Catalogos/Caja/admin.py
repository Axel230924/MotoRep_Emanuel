from django.contrib import admin
from .models import Caja

@admin.register(Caja)
class CajaAdmin(admin.ModelAdmin):

    search_fields = ['NumCaja']
    list_display = ['NumCaja']
