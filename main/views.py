from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from .forms import OficinaForm, AreaForm, ConfigureForm,TipoEquipoForm
from .models import Perfil, Oficina, Area, Configure, TipoEquipo

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
                print(user)
                user.save()
                print(user)
                login(request,user)
                #user = User.objects.last()
                perfil = Perfil.objects.create(user=user,perfil = request.POST['perfil'],nroCelular = request.POST['nroCelular'])
                perfil.save()
                print(perfil)
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
     
def configure(request):
    configures = Configure.objects.all()
    return render(request, 'configure.html',{
        'configures': configures
    })

def configure_create(request):
    if request.method == 'GET':
        return render(request,'configure_create.html',{
        'form' : ConfigureForm
        })
    else:
        try:
            form = ConfigureForm(request.POST)
            new_configure = form.save(commit=False)
            new_configure.save()
            return redirect('configure')
        except ValueError:
            return render(request, 'configure_create.html',{
                'form' :ConfigureForm,
                'error': 'Ingresar todos los datos requeridos'
            })
        
def configure_detail(request, configure_id):
    if request.method == 'GET':
        configure = get_object_or_404 (Configure, pk=configure_id)
        form = ConfigureForm(instance=configure)
        return render(request,'configure_detail.html', {'configure' : configure, 'form' : form})
    else:
       try:
        configure = get_object_or_404 (Configure, pk=configure_id)
        form =ConfigureForm(request.POST, instance=configure)
        form.save()
        return redirect('configure')
       except ValueError:
        return render(request,'configure_detail.html', {'configure' : configure, 'form' : form, 'error' : "Error Updating configure"})
       
def configure_delete(request, configure_id):
     configure = get_object_or_404 (Configure, pk=configure_id)
     if request.method == 'POST':
         configure.delete()
         return redirect('configure')
     
def tipoEquipo(request):
    tiposEquipos = TipoEquipo.objects.all()
    return render(request, 'tipoEquipo.html',{
        'tiposEquipos': tiposEquipos
    })

def tipoEquipo_create(request):
    if request.method == 'GET':
        return render(request,'tipoEquipo_create.html',{
        'form' : TipoEquipoForm
        })
    else:
        try:
            form = TipoEquipoForm(request.POST)
            new_tipoEquipo = form.save(commit=False)
            new_tipoEquipo.save()
            return redirect('tipoEquipo')
        except ValueError:
            return render(request, 'tipoEquipo_create.html',{
                'form' :TipoEquipoForm,
                'error': 'Ingresar todos los datos requeridos'
            })
        
def tipoEquipo_detail(request, tipoEquipo_id):
    if request.method == 'GET':
        tipoEquipo = get_object_or_404 (TipoEquipo, pk=tipoEquipo_id)
        form = TipoEquipoForm(instance=tipoEquipo)
        return render(request,'tipoEquipo_detail.html', {'tipoEquipo' : tipoEquipo, 'form' : form})
    else:
       try:
        tipoEquipo = get_object_or_404 (TipoEquipo, pk=tipoEquipo_id)
        form =ConfigureForm(request.POST, instance=tipoEquipo)
        form.save()
        return redirect('tipoEquipo')
       except ValueError:
        return render(request,'tipoEquipo_detail.html', {'tipoEquipo' : tipoEquipo, 'form' : form, 'error' : "Error Updating configure"})

def tipoEquipo_delete(request, tipoEquipo_id):
     tipoEquipo = get_object_or_404 (TipoEquipo, pk=tipoEquipo_id)
     if request.method == 'POST':
         tipoEquipo.delete()
         return redirect('tipoEquipo')