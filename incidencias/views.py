from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from main.models import Oficina, Area, Equipo
from equipos.models import ModelEquipo, ModelTipoEquipo
from .services import get_username

# Create your views here.
def newtask(request):
    trabajadores = User.objects.all()
    oficinas = Oficina.objects.filter(activo = True)
    areas = Area.objects.filter(activo = True)
    template_name = 'task.html'
    contexto = {'trabajadores':trabajadores, 'oficinas' :oficinas, 'areas' : areas}

    return render(request,template_name,contexto)

def list_equipos(_request):
    equipos = list(Equipo.objects.values())
    data = {'equipos' : equipos}
    return JsonResponse(data)

def search_equipo(request,codPatrimonial_id):
    equipos = list(ModelEquipo.objects.filter(codInterno= codPatrimonial_id).values())
    tipo = list(ModelTipoEquipo.objects.filter(idTipoEquipo= equipos[0]['codTipoBien']).values())

    #tipo = list(ModelTipoEquipo.objects.get(codInterno= codPatrimonial_id).values())
    data = {'equipos' : equipos,
            'tipo' : tipo
            }
    return JsonResponse(data)

def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'hello_user.html', context)