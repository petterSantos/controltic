from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.CharField(max_length=100)
    nroCelular = models.CharField(max_length=12, default='000000000')
    def __str__(self):
        return self.perfil+' - '+self.user.username

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

class Configure(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=500)
    def __str__(self):
        return self.key
