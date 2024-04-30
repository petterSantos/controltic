from django.contrib import admin
from .models import Perfil, Oficina, Area, Configure

# Register your models here.
admin.site.register(Oficina)
admin.site.register(Area)
admin.site.register(Perfil)
admin.site.register(Configure)