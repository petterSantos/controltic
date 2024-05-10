from django.forms import ModelForm
from .models import Oficina, Area, Configure,TipoEquipo, Equipo

""" class PerfilForm(ModelForm):    
    class Meta:
        model = Perfil
        fields = ['perfil', 'activo']
 """
class OficinaForm(ModelForm):    
    class Meta:
        model = Oficina
        fields = ['oficina','abrev','activo']

class AreaForm(ModelForm):    
    class Meta:
        model = Area
        fields = ['area','activo']
class ConfigureForm(ModelForm):    
    class Meta:
        model = Configure
        fields = ['key','value']

class TipoEquipoForm(ModelForm):    
    class Meta:
        model = TipoEquipo
        fields = ['tipo','descripcion','activo']


class EquipoForm(ModelForm):    
    class Meta:
        model = Equipo
        fields = [ 'marca','modelo','codPatrimonial','descripcionEquipo','descripcionCompra','estadoPatrimonio','responsablePatri',
                    'oficinaPatri','fechaUpdate','tipoEquipo','esPatrimonizado']