from django.urls import path
from . import views

urlpatterns = [
    path('queryEquipo/',views.queryEquipo, name='queryEquipo'),
]
