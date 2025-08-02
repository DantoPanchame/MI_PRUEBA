from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)

    ROL_CHOICES = (
        ('huesped', 'Huésped'),
        ('anfitrion', 'Anfitrión'),
    )
    rol_actual = models.CharField(max_length=20, choices=ROL_CHOICES, default='huesped')

    def __str__(self):
        return self.username
