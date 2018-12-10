from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'core/home.html',
    )

def listas(request):
    return render(request, 'core/listas.html',
    )

def detalle(request):
    return render(request, 'core/detalle.html',
    )

def productos(request):
    tienda = Tienda.objects.all()
    producto = Producto.objects.all()
    variables = {
        'tienda':tienda,
        'producto':producto
    }

    if request.POST:
        detProducto = Detalle_Producto()
        producto = Producto()
        # producto.nombre = request.POST.get(txtNombre)
        tienda = Tienda()
        tienda.id = request.POST.get(cboTienda)
        detProducto.nota_adicional = request.POST.get(txtNotaAdicional)
        detProducto.costo_real = request.POST.get(txtCostoReal)
        producto.id =request.POST.get(cboProducto)
        detProducto.fecha_valorizacion = request.POST.get(txtFecValoriza)

        try:
            producto.save()
            detProducto.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/productos.html',variables
    )

def tiendas(request):
    ciudad = Ciudad.objects.all()
    estado = Estado_tienda.objects.all()
    usuario = User.objects.all()
    variables = {
        'ciudad':ciudad,
        'estado':estado
        # 'usuario':usuario
    }

    if request.POST:
        tienda = Tienda()
        tienda.nombre = request.POST.get(txtNombre)
        tienda.nombre_sucursal = request.POST.get(txtNombreSucursal)
        tienda.direccion = request.POST.get(txtDireccion)
        ciudad=Ciudad()
        ciudad.id=request.POST.get(cboCiudad)
        tienda.website = request.POST.get(txtWeb)
        estado=Estado_tienda()
        estado.id=request.POST.get(cboEstado)
        usuario=User()
        usuario.id=request.POST.get(cboUsuario)


        try:
            producto.save()
            detProducto.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/tiendas.html',variables
    )
