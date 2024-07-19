from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from main.models import Oficina, Area, Equipo
from equipos.models import ModelEquipo, ModelTipoEquipo, ModelOficina, ModelPersona, ModelInventario
from main.models import Equipo, TipoEquipo
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

def search_bien(request,codBien_id):
    equipos = list(ModelEquipo.objects.filter(codInterno= codBien_id).values())
    tipo = list(ModelTipoEquipo.objects.filter(idTipoEquipo= equipos[0]['codTipoBien']).values())

    #tipo = list(ModelTipoEquipo.objects.get(codInterno= codPatrimonial_id).values())
    data = {'equipos' : equipos,
            'tipo' : tipo
            }
    return JsonResponse(data)

def search_equipo(request,codPatrimonial_id):
    equipos = list(ModelEquipo.objects.filter(codInterno= codPatrimonial_id).values())
    if equipos[0]['codTipoBien']:
        codEquipo = equipos[0]['idEquipo']
        #buscando tipo
        tipo = list(ModelTipoEquipo.objects.filter(idTipoEquipo= equipos[0]['codTipoBien']).values())
        if tipo:
            tipoSend = tipo[0]['tipo']
        #buscando oficina y responsable
        inventarios = list(ModelInventario.objects.filter(idInventario = codEquipo).values())
        print(inventarios)
        data = {'equipos' : equipos,
            'tipoSend' : tipo,
            'inventarios' : inventarios
            }
        return JsonResponse(data)
    else:
        print('no se enontro bien')

        data = {'equipos' : 'equipos',
            'tipoSend' : 'tipo',
            'inventarios' : 'inventarios'
            }
        return JsonResponse(data)
    return None

def search_equipoInterno(request,codPatrimonial_id):
    equipos = list(Equipo.objects.filter(codPatrimonial= codPatrimonial_id).values())
    tipo = list(TipoEquipo.objects.filter(id= equipos[0]['tipoEquipo_id']).values())
    data = {'equipos' : equipos,
             'tipo' : tipo[0]['tipo'] }
    return JsonResponse(data)

def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'hello_user.html', context)