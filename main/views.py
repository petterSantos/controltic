from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.utils import timezone
from .forms import PerfilForm
from .models import Perfil

# Create your views here.
def home(request):
    return render(request,'home.html')

def perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfiles.html',{
        'perfiles':perfiles
    })

def create_perfil(request):
    if request.method == 'GET':
        return render(request,'create_perfil.html',{
        'form' : PerfilForm
        })
    else:
        try:
            form = PerfilForm(request.POST)
            new_perfil = form.save(commit=False)
            new_perfil.save()
            return redirect('perfiles')
        except ValueError:
            return render(request, 'create_perfil.html',{
                'form' :PerfilForm,
                'error': 'Ingresar todos los datos requeridos'
            })
        