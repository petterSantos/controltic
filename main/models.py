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

class TipoEquipo(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.tipo

class Equipo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    codPatrimonial = models.CharField(max_length=20)
    descripcionEquipo =  models.TextField(blank=True)
    descripcionCompra =  models.TextField(blank=True)
    estadoPatrimonio = models.CharField(max_length=1) # M R B
    responsablePatri = models.CharField(max_length=100)
    oficinaPatri = models.CharField(max_length=100)
    fechaUpdate = models.DateTimeField(null=True)
    tipoEquipo = models.ForeignKey(TipoEquipo,on_delete=models.CASCADE)
    esPatrimonizado = models.BooleanField(default=False)
    def __str__(self):
        return self.marca+' - '+self.modelo+' by '+self.responsablePatri

class Incidencia(models.Model):
    solicita = models.CharField(max_length=100)
    oficina = models.ForeignKey(Oficina,on_delete=models.CASCADE)
    solicitante = models.CharField(max_length=100)
    codSolicitante = models.IntegerField(null=False)
    cargoUsuario = models.CharField(max_length=100)
    solicitaConDoc =models.BooleanField(default=False)
    nroDoc = models.CharField(max_length=400, blank = True, null=True)
    fechaSolicita = models.DateTimeField(auto_now_add=True)
    dejaEquipo =models.BooleanField(default=False)
    userTic = models.ForeignKey(User,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    fechaTermina = models.DateTimeField(null=True)
    def __str__(self):
        return self.key
