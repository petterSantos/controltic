"""
URL configuration for proycontroltic project.

The `urlpatterns` list routes URLs to  For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function     1. Add an import:  from my_app import     2. Add a URL to urlpatterns:  path('', home, name='home')
Class-based     1. Add an import:  from other_app.import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from maintenance import as viewmaintenance
from main.views import home,signup,oficinas,oficina_create,oficina_detail,oficina_delete,areas,area_create,area_detail,area_delete,configure,configure_create,configure_delete,configure_detail,tipoEquipo,tipoEquipo_create,tipoEquipo_delete,tipoEquipo_detail
from equipos.views import queryEquipo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('signup/', signup,name='signup'),
    #path('perfil/create/',perfil_create,name='perfil_create'),
    #path('perfil/',perfiles,name='perfiles'),
    #path('perfil/<int:perfil_id>/', perfil_detail, name='perfil_detail'),
    #path('perfil/<int:perfil_id>/delete', perfil_delete, name='perfil_delete'),
    path('oficina/',oficinas,name='oficinas'),
    path('oficina/create/',oficina_create,name='oficina_create'),
    path('oficina/<int:oficina_id>/', oficina_detail, name='oficina_detail'),
    path('oficina/<int:oficina_id>/delete', oficina_delete, name='oficina_delete'),
    path('area/',areas,name='areas'),
    path('area/create/',area_create,name='area_create'),
    path('area/<int:area_id>/', area_detail, name='area_detail'),
    path('area/<int:area_id>/delete', area_delete, name='area_delete'),
    path('configure/',configure,name='configure'),
    path('configure/create/',configure_create,name='configure_create'),
    path('configure/<int:configure_id>/', configure_detail, name='configure_detail'),
    path('configure/<int:configure_id>/delete', configure_delete, name='configure_delete'),
    path('tipoEquipo/',tipoEquipo,name='tipoEquipo'),
    path('tipoEquipo/create/',tipoEquipo_create,name='tipoEquipo_create'),
    path('tipoEquipo/<int:tipoEquipo_id>/', tipoEquipo_detail, name='tipoEquipo_detail'),
    path('tipoEquipo/<int:tipoEquipo_id>/delete', tipoEquipo_delete, name='tipoEquipo_delete'),
    path('queryEquipo/',queryEquipo, name='queryEquipo'),
]
