from django.contrib import admin
from .models import Perfil, Oficina, Area, Configure, TipoEquipo, Equipo

# Register your models here.
admin.site.register(Oficina)
admin.site.register(Area)
admin.site.register(Perfil)
admin.site.register(Configure)
admin.site.register(TipoEquipo)
admin.site.register(Equipo)