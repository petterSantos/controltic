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

""" def buscar TipoEqupo():
    try:
        equipo = list(ModelEquipo.objects.values)
        data = {'equipo' : equipo}
        return JsonResponse(data)
    except """

def buscarEquipo(request):
    try:
        equipo = list(ModelEquipo.objects.get(codInterno= request.POST.get('codPatrimonial',None)))
        data = {'equipo' : equipo}
        return JsonResponse(data)
    except ModelEquipo.DoesNotExist:
        equipo = None
        #tipoEquipo = None
        return render(request, 'seleccioneEquipo.html',{
                'error': 'No se encontro ninguna referencia',
                'equipo': equipo
        })


def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'hello_user.html', context)