from django.urls import path
from . import views
urlpatterns =  [
         path('newtask/',views.newtask,name='newtask'),
         path('list_equipos/',views.list_equipos,name='list_equipos'),
       #  path('search_equipo/',views.list_equipos,name='list_equipos')
        path('search_equipo/<str:codPatrimonial_id>/', views.search_equipo, name='search_equipo'),
        path('search_equipoInterno/<str:codPatrimonial_id>/', views.search_equipoInterno, name='search_equipo'),
         path('search_bien/<str:codBien_id>/', views.search_bien, name='search_bien'),
        path('hello/',views.hello_user,name='hello')
]