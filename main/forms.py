from django import forms
from .models import Oficina, Area, Configure,TipoEquipo, Equipo

""" class PerfilForm(forms.ModelForm):    
    class Meta:
        model = Perfil
        fields = ['perfil', 'activo']
 """
ACTIVADO = {True: "ACTIVO", False: "DESACTIVADO"}
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
        widgets ={
                'area': forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribir un Area TIC'}),
                'activo': forms.CheckboxInput(attrs={'class':'form-check-input m-auto mt-2'})
        } 

class ConfigureForm(forms.ModelForm):    
    class Meta:
        model = Configure
        fields = ['key','value']

class TipoEquipoForm(forms.ModelForm):    
    class Meta:
        model = TipoEquipo
        fields = ['tipo','descripcion','activo']
        widgets ={
                'tipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'escribir el tipo de equipo'}),
                'descripcion':  forms.Textarea(attrs={'class':'form-control', 'placeholder':'escribir usa descripcion'}),
                'activo': forms.CheckboxInput(attrs={'class':'form-check-input m-auto mt-2'})
        }      


class EquipoForm(forms.ModelForm):    
    class Meta:
        model = Equipo
        fields = [ 'marca','modelo','codPatrimonial','descripcionEquipo','descripcionCompra','estadoPatrimonio','responsablePatri',
                    'oficinaPatri','fechaUpdate','tipoEquipo','esPatrimonizado']