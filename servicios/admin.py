from django.contrib import admin
from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('creado','actualizado') #estos datos aparecen de forma informativa
    
admin.site.register(Servicio, ServicioAdmin)

