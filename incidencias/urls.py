from django.urls import path
from . import views
urlpatterns =  [
         path('newtask/',views.newtask,name='newtask')
]