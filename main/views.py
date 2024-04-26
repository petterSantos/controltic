from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from .forms import OficinaForm, AreaForm
from .models import Perfil, Oficina, Area

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET' :
       return render(request,'signup.html',{
             'form': UserCreationForm
       })
    else:
         if request.POST['password1'] == request.POST['password2'] :
           try:
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'],
                                                first_name = request.POST['first_name'], last_name = request.POST['last_name'],
                                                email = request.POST['email'], is_staff = True, is_active = True)
                user.save()
                login(request,user)
                user = User.objects.last()
                perfil = Perfil.objects.create(user=user,perfil = request.POST['perfil'],nroCelular = request.POST['nroCelular'])
                perfil.save()
                return redirect('home')
               ## return HttpResponse('User Created Successify')
           except IntegrityError:
               return render(request, 'signup.html',{
                   'form' : UserCreationForm,
                   'error': 'Username already exists'
               })

         return render(request, 'signup.html',{
                   'form' : UserCreationForm,
                   'error': 'Password do no match'
               }) 

def perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfiles.html',{
        'perfiles':perfiles
    })

def perfil_create(request):
    if request.method == 'GET':
        return render(request,'perfil_create.html',{
        'form' : PerfilForm
        })
    else:
        try:
            form = PerfilForm(request.POST)
            new_perfil = form.save(commit=False)
            new_perfil.save()
            return redirect('perfiles')
        except ValueError:
            return render(request, 'perfil_create.html',{
                'form' :PerfilForm,
                'error': 'Ingresar todos los datos requeridos'
            })
        
def perfil_detail(request, perfil_id):
    if request.method == 'GET':
        perfil = get_object_or_404 (Perfil, pk=perfil_id)
        form = PerfilForm(instance=perfil)
        return render(request,'perfil_detail.html', {'perfil' : perfil, 'form' : form})
    else:
       try:
        perfil = get_object_or_404 (Perfil, pk=perfil_id)
        form = PerfilForm(request.POST, instance=perfil)
        form.save()
        return redirect('perfiles')
       except ValueError:
        return render(request,'perfil_detail.html', {'perfil' : perfil, 'form' : form, 'error' : "Error Updating perfil"})

def perfil_delete(request, perfil_id):
     perfil = get_object_or_404 (Perfil, pk=perfil_id)
     if request.method == 'POST':
         perfil.delete()
         return redirect('perfiles')

def oficinas(request):
    oficinas = Oficina.objects.all()
    return render(request, 'oficinas.html',{
        'oficinas': oficinas
    })

def oficina_create(request):
    if request.method == 'GET':
        return render(request,'oficina_create.html',{
        'form' : OficinaForm
        })
    else:
        try:
            form = OficinaForm(request.POST)
            new_oficina = form.save(commit=False)
            new_oficina.save()
            return redirect('oficinas')
        except ValueError:
            return render(request, 'oficina_create.html',{
                'form' :OficinaForm,
                'error': 'Ingresar todos los datos requeridos'
            })
        
def oficina_detail(request, oficina_id):
    if request.method == 'GET':
        oficina = get_object_or_404 (Oficina, pk=oficina_id)
        form = OficinaForm(instance=oficina)
        return render(request,'oficina_detail.html', {'oficina' : oficina, 'form' : form})
    else:
       try:
        oficina = get_object_or_404 (Oficina, pk=oficina_id)
        form = OficinaForm(request.POST, instance=oficina)
        form.save()
        return redirect('oficinas')
       except ValueError:
        return render(request,'oficina_detail.html', {'oficina' : oficina, 'form' : form, 'error' : "Error Updating oficina"})
       
def oficina_delete(request, oficina_id):
     oficina = get_object_or_404 (Oficina, pk=oficina_id)
     if request.method == 'POST':
         oficina.delete()
         return redirect('oficinas')
     
def areas(request):
    areas = Area.objects.all()
    return render(request, 'areas.html',{
        'areas': areas
    })

def area_create(request):
    if request.method == 'GET':
        return render(request,'area_create.html',{
        'form' : AreaForm
        })
    else:
        try:
            form = AreaForm(request.POST)
            new_area = form.save(commit=False)
            new_area.save()
            return redirect('areas')
        except ValueError:
            return render(request, 'area_create.html',{
                'form' :AreaForm,
                'error': 'Ingresar todos los datos requeridos'
            })
        
def area_detail(request, area_id):
    if request.method == 'GET':
        area = get_object_or_404 (Area, pk=area_id)
        form = AreaForm(instance=area)
        return render(request,'area_detail.html', {'area' : area, 'form' : form})
    else:
       try:
        area = get_object_or_404 (Area, pk=area_id)
        form = AreaForm(request.POST, instance=area)
        form.save()
        return redirect('areas')
       except ValueError:
        return render(request,'area_detail.html', {'area' : area, 'form' : form, 'error' : "Error Updating area"})
       
def area_delete(request, area_id):
     area = get_object_or_404 (Area, pk=area_id)
     if request.method == 'POST':
         area.delete()
         return redirect('areas')