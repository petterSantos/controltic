from django.forms import ModelForm
from .models import Oficina, Area

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