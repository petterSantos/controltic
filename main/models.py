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
    codPatrimonial = models.CharField(max_length=20,blank=True)
    codInterno = models.CharField(max_length=20,blank=True)
    marca = models.CharField(max_length=50, blank=True)
    modelo = models.CharField(max_length=50, blank=True)
    nroSerie = models.CharField(max_length=25, blank=True)
    color = models.CharField(max_length=20, blank=True)
    fechaPecosa = models.DateField(null=True)
    estado = models.CharField(max_length=1)
    tipoDocAdq = models.CharField(max_length=15, blank=True)
    nroDocAdq = models.CharField(max_length=50, blank=True)
    regSiaf = models.CharField(max_length=10, blank=True)
    descripcionEquipo =  models.TextField(blank=True)
    responsablePatri = models.CharField(max_length=100, blank=True)
    oficinaPatri = models.CharField(max_length=150,blank= True)
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
