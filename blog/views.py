from django.shortcuts import render
from .models import Post
def blog(request):
    posts = Post.objects.all().order_by('-creado')  # Ordenar por fecha de creación (más reciente primero)
    vista = request.GET.get('vista', 'lista')  # Obtener el parámetro 'vista' de la URL, por defecto es 'list'
    return render(request, "ProyectoWebApp/blog.html", {"posts": posts, "vista": vista})
    
    
#vista en cards cajonsitos
#vista carrucel

