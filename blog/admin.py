from django.contrib import admin
from .models import Categoria, Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado') 

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado') 
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

#tablas para administaralas en la base de datos Y en el el panes django




