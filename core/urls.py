from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('', home, name="home"),
    path('listas/', listas, name="listas"),
    path('productos/', productos, name="productos"),
    path('tiendas/', tiendas, name="tiendas"),
    path('producto-add/<id>/', detalleLista, name="producto-add"),
]
