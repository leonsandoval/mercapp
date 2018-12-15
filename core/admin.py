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

class EstadoTiendaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')    

class TiendaAdmin(admin.ModelAdmin):
    list_display = ('nombre','nombre_sucursal' ,'direccion','id_ciudad' ,'website','id_estado' ,'id_usuario')
    
class ListaAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,'cant_productos','total_presupuestado','total_real')
  

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Detalle_Producto, DetProductoAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Estado_tienda, EstadoTiendaAdmin)
admin.site.register(Tienda, TiendaAdmin)
admin.site.register(Lista, ListaAdmin)