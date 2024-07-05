from equipos.models import ModelEquipo, ModelTipoEquipo
import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_username(params={}):
    response = generate_request('https://randomuser.me/api', params)
    if response:
       user = response.get('results')[0]
       return user.get('name').get('first')

    return "''"

def get_equipo(cod,params={}):
    try:
        equipo = ModelEquipo.objects.get(codInterno= cod)
        try:
            tipoEquipo =ModelTipoEquipo.objects.get(idTipoEquipo=equipo.codTipoBien)
            context = {'equipo': equipo, 'tipoEquipo': tipoEquipo}
            return context
        except  ModelTipoEquipo.DoesNotExist:
                 equipo = None
                 tipoEquipo = None
                 context = {'equipo': equipo, 'tipoEquipo': tipoEquipo}
                 return context  
    except ModelEquipo.DoesNotExist:
        equipo = None
        tipoEquipo = None
        context = {'equipo': equipo, 'tipoEquipo': tipoEquipo}
        return context
