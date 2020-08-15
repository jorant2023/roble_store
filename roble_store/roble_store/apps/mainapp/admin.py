from django.contrib import admin
from .models import  Categorias, Productos, Proveedores
# Register your models here.


admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(Proveedores)