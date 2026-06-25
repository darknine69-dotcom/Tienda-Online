from django.urls import path, include 
from . import views 
from . views import Vregistro

urlpatterns = [
    path('autenticacion/', Vregistro.as_view(), name="autenticacion"), #genera automaticamente las entradas
]
