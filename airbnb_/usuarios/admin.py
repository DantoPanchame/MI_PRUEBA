from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('username', 'email', 'rol_actual', 'is_staff', 'is_active')
    list_filter = ('rol_actual', 'is_staff', 'is_active')

admin.site.register(Usuario, UsuarioAdmin)
