from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout


User = get_user_model()


def login_metodo(request):
    # Pantalla 1: Elegir método de autenticación (solo correo funciona)
    return render(request, 'usuarios/login_metodo.html')

def ingresar_email(request):
    if request.method == "POST":
        email = request.POST.get("email").strip().lower()
        
        # Buscar si existe un usuario con este correo
        usuario_existente = User.objects.filter(email=email).first()
        
        if usuario_existente:
            # Guardamos temporalmente el email en la sesión para usarlo en la siguiente vista
            request.session['email_temp'] = email
            # ✅ Ahora redirige a la versión estilizada
            return redirect(reverse('usuarios:login_usuario'))
        else:
            # Guardamos temporalmente el email en la sesión para precargarlo en el registro
            request.session['email_temp'] = email
            return redirect(reverse('usuarios:registro_usuario'))
    
    return render(request, 'usuarios/ingresar_email.html')



def registro_usuario(request):
    # Recuperamos email de la sesión
    email_temp = request.session.get('email_temp', '')

    if request.method == "POST":
        nombre = request.POST.get("first_name")
        apellido = request.POST.get("last_name")
        fecha_nacimiento = request.POST.get("birthdate")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Crear el nuevo usuario
        nuevo_usuario = User.objects.create_user(
            username=email,      # usamos el correo como username
            email=email,
            first_name=nombre,
            last_name=apellido,
            password=password
        )

        # Podríamos guardar la fecha de nacimiento en otro modelo extra si queremos

        # Logueamos automáticamente
        login(request, nuevo_usuario)

        # Redirigimos a compromiso de comunidad
        return redirect(reverse('usuarios:compromiso_comunidad'))

    # ✅ Aquí pasamos 'email' para que el HTML lo use con {{ email }}
    return render(request, 'usuarios/registro_usuario.html', {'email': email_temp})


def compromiso_comunidad(request):
    if request.method == "POST":
        # Si hace clic en aceptar, lo llevamos al home
        return redirect('/')  # Aquí va la vista home del proyecto

    return render(request, 'usuarios/compromiso_comunidad.html')

def login_contraseña(request):
    email_temp = request.session.get('email_temp', '')
    usuario = User.objects.filter(email=email_temp).first()

    if not usuario:
        # Si no hay usuario en sesión, volvemos a pedir correo
        return redirect(reverse('usuarios:ingresar_email'))

    error = None

    if request.method == "POST":
        password = request.POST.get('password')
        
        # Autenticamos con email (como username)
        usuario_auth = authenticate(request, username=email_temp, password=password)

        if usuario_auth:
            # Contraseña correcta → loguear
            login(request, usuario_auth)
            return redirect('/')  # Home
        else:
            error = "Contraseña incorrecta. Intenta de nuevo."

    return render(request, 'usuarios/login_contraseña.html', {
        'usuario': usuario,
        'error': error
    })
    
def cerrar_sesion(request):
    logout(request)  # Elimina la sesión del usuario
    return redirect('usuarios:ingresar_email')  # Lo mandamos a la pantalla inicial

    from django.contrib.auth import authenticate, login

def login_usuario(request):
    # Recuperamos el correo guardado en sesión desde ingresar_email
    email_temp = request.session.get('email_temp', '')

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Intentar autenticar
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # luego podemos cambiar la redirección si quieres
        else:
            return render(
                request,
                'usuarios/login_usuario.html',
                {
                    'email': email_temp,
                    'error': 'Contraseña incorrecta. Inténtalo de nuevo.'
                }
            )

    # GET → mostrar el formulario
    return render(request, 'usuarios/login_usuario.html', {'email': email_temp})
