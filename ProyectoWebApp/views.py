from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from blog.models import Post
# from servicios.models import Servicio

def home(request):
    return render(request, "ProyectoWebApp/home.html")

# def servicios(request):
#     servi = Servicio.objects.all()
#     return render(request, "ProyectoWebApp/servicios.html", {"servi": servi})

     
def blog(request):
    posts = Post.objects.all().order_by('-creado')  # Ordenar por fecha de creación (más reciente primero)
    vista = request.GET.get('vista', 'lista')  # Obtener el parámetro 'vista' de la URL, por defecto es 'list'
    return render(request,"ProyectoWebApp/blog.html", {"posts": posts, "vista": vista})



# def tienda(request):
#     return render(request,"ProyectoWebApp/tienda.html")


def contactos(request):
    if request.method == 'POST':
        asunto=request.POST.get("asunto")
        email=request.POST.get("email")
        mensaje=request.POST.get("mensaje")
        mensaje_user = f"""Email del usuario:{email} Mensaje:{mensaje}"""
        send_mail(
            asunto,
            mensaje_user,
            settings.EMAIL_HOST_USER,
            ["darknine69@gmail.com"],
            fail_silently=False
        )
        return render(request,"ProyectoWebApp/contactos.html", {"valido": True})
    return render (request,"ProyectoWebApp/contactos.html")        


# Create tree views
#vista en lista datos
# def blog_list(request):
#     lista_post=Post.objects.all()
#     return render(request,'proyectoWebApp/blog.html',{'posts':lista_post})

# def blog_carrucel(request):
#     lista_post=Post.objects.all()
#     return render(request,'blog_carrucel.html',{'lista_post':lista_post})  

# def blog_cards(request):    
#     lista_post=Post.objects.all()
#     return render(request,'blog_cards.html',{'lista_post':lista_post})
