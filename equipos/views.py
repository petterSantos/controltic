from django.shortcuts import render, redirect, get_object_or_404
from .models import ModelEquipo, ModelTipoEquipo
#from .forms import OficinaForm, AreaForm, ConfigureForm,TipoEquipoForm, EquipoForm

def queryEquipo(request):
    if request.method == 'GET':
        return render(request,'queryEquipo.html')
    else:
        try:
            print(request.POST)
            #equipos =  ModelEquipo.objects.all()
            #print(equipos)
            equipoEncontrado = ModelEquipo.objects.get(codInterno= request.POST.get('codPatrimonial',None))
            print(equipoEncontrado)
            print('TipoCod: ' + equipoEncontrado.codTipoBien)
            if equipoEncontrado:
                tipoEquipo = ModelTipoEquipo.objects.get(idTipoEquipo=equipoEncontrado.codTipoBien)
                print(tipoEquipo)

            return render(request, 'queryEquipo.html',{
                'equipo': equipoEncontrado,
                'tipo': tipoEquipo
            })
           # form = EquipoForm(request.POST)
           # new_equipo = form.save(commit=False)
           # new_equipo.save()
           # return redirect('equipos')
        except ValueError:
            return render(request, 'queryEquipo.html',{
                'error': 'Ingresar todos los datos requeridos'
            })
    return render(request, 'queryEquipo.html')
