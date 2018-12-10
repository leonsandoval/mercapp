from django.contrib import admin
from .models import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', )

class DetProductoAdmin(admin.ModelAdmin):
    list_display = ('id','id_tienda','nota_adicional','costo_real','id_producto','fecha_valorizacion' )

class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', )

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','id_region')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle_Producto, DetProductoAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Ciudad, CiudadAdmin)
