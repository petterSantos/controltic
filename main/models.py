from django.db import models

# Create your models here.
class Perfil(models.Model):
    perfil = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.perfil