from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto

def agregar_producto(request, producto_id):
    carro = Carro(request)
    identificador = Producto.objects.get(id=producto_id)
    carro.agregar(producto=identificador)
    return redirect("Tienda") #para q no se salga de la url

#creacion de la primer vista 

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    identificador = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=identificador)
    return redirect("Tienda") #para q no se salga de la url
    

def restar_producto(request, producto_id):
    carro = Carro(request)
    identificador = Producto.objects.get(id=producto_id)
    carro.restar(producto=identificador)
        
    return redirect("Tienda") 

  
def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return  redirect("Tienda")

    
    
    
