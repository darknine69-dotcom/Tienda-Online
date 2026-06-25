from django.shortcuts import render
from .models import CategoriaProd, Producto

# from django.contrib.admin .views.decorators import staff_member_required #debo estar logeado como super usuario para ingresar a esta vista


def tienda(request):
    productos = Producto.objects.all()
    return render(request,"tienda.html",{"productos": productos})

