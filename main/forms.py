from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Perfil, Oficina, Area

User = get_user_model()
class FormularioRegistroUsuarioPersonalizado(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password','paterno']
class PerfilForm(ModelForm):    
    class Meta:
        model = Perfil
        fields = ['perfil', 'activo']

class OficinaForm(ModelForm):    
    class Meta:
        model = Oficina
        fields = ['oficina','abrev','activo']

class AreaForm(ModelForm):    
    class Meta:
        model = Area
        fields = ['area','activo']