"""
URL configuration for proycontroltic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#from maintenance import views as viewmaintenance
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/', views.signup,name='signup'),
    #path('perfil/create/',views.perfil_create,name='perfil_create'),
    #path('perfil/',views.perfiles,name='perfiles'),
    #path('perfil/<int:perfil_id>/', views.perfil_detail, name='perfil_detail'),
    #path('perfil/<int:perfil_id>/delete', views.perfil_delete, name='perfil_delete'),
    path('oficina/',views.oficinas,name='oficinas'),
    path('oficina/create/',views.oficina_create,name='oficina_create'),
    path('oficina/<int:oficina_id>/', views.oficina_detail, name='oficina_detail'),
    path('oficina/<int:oficina_id>/delete', views.oficina_delete, name='oficina_delete'),
    path('area/',views.areas,name='areas'),
    path('area/create/',views.area_create,name='area_create'),
    path('area/<int:area_id>/', views.area_detail, name='area_detail'),
    path('area/<int:area_id>/delete', views.area_delete, name='area_delete'),
    path('configure/',views.configure,name='configure'),
    path('configure/create/',views.configure_create,name='configure_create'),
    path('configure/<int:configure_id>/', views.configure_detail, name='configure_detail'),
    path('configure/<int:configure_id>/delete', views.configure_delete, name='configure_delete'),
    path('tipoEquipo/',views.tipoEquipo,name='tipoEquipo'),
    path('tipoEquipo/create/',views.tipoEquipo_create,name='tipoEquipo_create'),
    path('tipoEquipo/<int:tipoEquipo_id>/', views.tipoEquipo_detail, name='tipoEquipo_detail'),
    path('tipoEquipo/<int:tipoEquipo_id>/delete', views.tipoEquipo_delete, name='tipoEquipo_delete'),
]
