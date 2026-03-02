from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
telefono_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="El teléfono debe contener exactamente 10 dígitos."
)

class Contacto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    telefono = models.CharField(
        max_length=10,
        validators=[telefono_validator]
    )
    Nota = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre