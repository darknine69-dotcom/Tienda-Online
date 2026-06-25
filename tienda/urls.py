from django.urls import path, include 
from . import views 

urlpatterns = [
    path('tienda/', views.tienda, name="Tienda"),
]
