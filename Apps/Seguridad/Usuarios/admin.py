from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from Apps.Seguridad.Usuarios.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    pass 