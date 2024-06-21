from django.shortcuts import render, redirect, get_object_or_404
from .models import ModelEquipo, ModelTipoEquipo

def queryEquipo(request):
    if request.method == 'GET':
        return render(request,'queryEquipo.html')
    else:
        try:
            equipoEncontrado = ModelEquipo.objects.get(codInterno= request.POST.get('codPatrimonial',None))
            print(equipoEncontrado)
            print('TipoCod: ' + equipoEncontrado.codTipoBien)
            try:
               tipoEquipo = ModelTipoEquipo.objects.get(idTipoEquipo=equipoEncontrado.codTipoBien)
               print(tipoEquipo)
               return render(request, 'queryEquipo.html',{
                 'equipo': equipoEncontrado,
                 'tipo': tipoEquipo
                })
            except ModelTipoEquipo.DoesNotExist:
                 equipoEncontrado = None
                 tipoEquipo = None
                 return render(request, 'queryEquipo.html',{
                    'error': 'No se encontro ninguna referencia',
                    'equipo': equipoEncontrado,
                    'tipo': tipoEquipo
                 })
        except ModelEquipo.DoesNotExist:
             equipoEncontrado = None
             tipoEquipo = None
             return render(request, 'queryEquipo.html',{
                'error': 'No se encontro ninguna referencia',
                'equipo': equipoEncontrado,
                'tipo': tipoEquipo
            })
    return render(request, 'queryEquipo.html')
