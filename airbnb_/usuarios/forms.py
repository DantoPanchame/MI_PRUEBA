from django import forms
from django.core.validators import MinLengthValidator
from datetime import date

class DatosPersonalesForm(forms.Form):
    nombre_legal = forms.CharField(
        label="Nombre legal",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre que aparece en tu identificación'})
    )
    apellidos_legales = forms.CharField(
        label="Apellidos legales",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Apellidos que aparecen en tu identificación'})
    )
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Debes ser mayor de 18 años."
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        validators=[MinLengthValidator(8)],
        help_text="Mínimo 8 caracteres."
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        # Validar que las contraseñas coincidan
        if cleaned_data.get('password1') != cleaned_data.get('password2'):
            raise forms.ValidationError("Las contraseñas no coinciden.")
        
        # Validar edad mínima (18 años)
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        if fecha_nacimiento:
            hoy = date.today()
            edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            if edad < 18:
                raise forms.ValidationError("Debes tener al menos 18 años para registrarte.")