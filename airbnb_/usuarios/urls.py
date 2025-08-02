from django.urls import path
from . import views
from .views import login_usuario  # si aún se usa para login directo

app_name = 'usuarios'

urlpatterns = [
    # ✅ Pantalla 1: Elegir método (Google, Apple, Correo)
    path('login/', views.login_metodo, name='login_metodo'),

    # ✅ Pantalla 2: Ingresar correo
    path('email/', views.ingresar_email, name='ingresar_email'),

    # ✅ Pantalla 3: Registro de usuario nuevo
    path('registro/', views.registro_usuario, name='registro_usuario'),

    # ✅ Pantalla 4: Compromiso comunidad
    path('compromiso/', views.compromiso_comunidad, name='compromiso_comunidad'),

    # ✅ Pantalla contraseña para usuarios existentes
    path('login-password/', views.login_contraseña, name='login_contraseña'),

    # ✅ Logout
    path('logout/', views.cerrar_sesion, name='logout'),

    # ✅ Login directo (solo si se necesita a futuro, no interfiere)
    path('login-directo/', login_usuario, name='login_usuario'),
]
