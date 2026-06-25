from django.db import models

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name = 'categoriaprod'
        verbose_name_plural = 'categoriasprod'
    
    def __str__(self):
        return self.nombre #aparece un mensaje la categoria creada junto con la fecha
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE) # elimine en cascada
    imagen = models.ImageField(upload_to='tienda', null=True, blank=True) # se guarda en esta carpeta, y puede no usarce
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True) #disponibilidad por defecto en true
    
    #agregar nuevos campos sin corromper el codigo
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
   
   
    class meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.nombre 


    
    
    
    
