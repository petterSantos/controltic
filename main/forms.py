from django import forms
from .models import Oficina, Area, Configure,TipoEquipo, Equipo

""" class PerfilForm(forms.ModelForm):    
    class Meta:
        model = Perfil
        fields = ['perfil', 'activo']
 """
class OficinaForm(forms.ModelForm):    
    class Meta:
        model = Oficina
        fields = ['oficina','abrev','activo']
        widgets ={
                'oficina': forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribir una Oficina'}),
                'abrev':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribir su Abreviatura'}),
                'activo': forms.CheckboxInput(attrs={'class':'form-check-input m-auto mt-2'})
        } 

class AreaForm(forms.ModelForm):    
    class Meta:
        model = Area
        fields = ['area','activo']
class ConfigureForm(forms.ModelForm):    
    class Meta:
        model = Configure
        fields = ['key','value']

class TipoEquipoForm(forms.ModelForm):    
    class Meta:
        model = TipoEquipo
        fields = ['tipo','descripcion','activo']


class EquipoForm(forms.ModelForm):    
    class Meta:
        model = Equipo
        fields = [ 'marca','modelo','codPatrimonial','descripcionEquipo','descripcionCompra','estadoPatrimonio','responsablePatri',
                    'oficinaPatri','fechaUpdate','tipoEquipo','esPatrimonizado']