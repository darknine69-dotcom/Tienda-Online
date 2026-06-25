from django.shortcuts import render, redirect
from django.views.generic import View
# from django.contrib.auth.forms import UserCreationForm => esto es por defecto del forms
from django.contrib.auth import login
from django.contrib import messages # lanzar ecesciones cuando registremos un usuario
from .forms import CustomUserCreationForm

# def autenticacion(request):
#     return render(request , "registro.html")

class Vregistro(View):
    
    def get(self, request):
        form = CustomUserCreationForm()
        return render (request, "registro.html", {"form":form})
   
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('Home')
        else: 
            for mensaje in form.error_messages:
                messages.error(request, form.error_messages[mensaje])
            return render (request, "registro.html", {"form":form})  
        
#cerrar seccion aparecer boton de registrado en aplicacion 
        
        