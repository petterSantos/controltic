from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import Oficina, Area

# Create your views here.
def newtask(request):
    trabajadores = User.objects.all()
    oficinas = Oficina.objects.filter(activo = True)
    areas = Area.objects.filter(activo = True)
    template_name = 'task.html'
    contexto = {'trabajadores':trabajadores, 'oficinas' :oficinas, 'areas' : areas}

    return render(request,template_name,contexto)