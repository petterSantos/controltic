from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UsuarioPersonalizado(AbstractUser):
    # Tus propiedades personalizadas
    paterno = models.CharField(max_length=30)
    
class Perfil(models.Model):
    perfil = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.perfil

class Oficina(models.Model):
    oficina = models.CharField(max_length=200)
    abrev = models.CharField(max_length=10)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.oficina

class Area(models.Model):
    area = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.area
