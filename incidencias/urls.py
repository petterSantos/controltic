from django.urls import path
from . import views
urlpatterns =  [
         path('newtask/',views.newtask,name='newtask'),
         path('list_equipos/',views.list_equipos,name='list_equipos')
]