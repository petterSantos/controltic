from django.urls import path
from . import views
urlpatterns =  [
         path('newtask/',views.newtask,name='newtask'),
         path('list_equipos/',views.list_equipos,name='list_equipos'),
       #  path('search_equipo/',views.list_equipos,name='list_equipos')
        path('buscarEquipo/',views.buscarEquipo,name='buscarEquipo'),
        path('hello/',views.hello_user,name='hello')
       

]