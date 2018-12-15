from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'core/home.html',
    )

# def listas(request):
#     return render(request, 'core/listas.html',
#     )

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
        detProducto.nota_adicional = request.POST.get('txtNotaAdicional')
        detProducto.costo_real = request.POST.get('txtCostoReal')
        detProducto.fecha_valorizacion = request.POST.get('txtFecValoriza')
        tienda = Tienda()
        tienda.id = request.POST.get('cboTienda')
        detProducto.id_tienda = tienda

        producto = Producto()
        producto.id = request.POST.get('cboProducto')
        detProducto.id_producto = producto
        
        try:
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


def listas(request):
    lista = Lista.objects.all()
    variables = {
        'lista':lista,
    }

    if request.POST:
        lista = Lista()
        # producto.nombre = request.POST.get(txtNombre)

        lista.nombre = request.POST.get(txtNombre)
        lista.cant_productos = request.POST.get(txtCantProd)
        lista.total_presupuestado =request.POST.get(txtTotalPres)
        lista.total_real = request.POST.get(txtTotalReal)

        try:
            producto.save()
            detProducto.save()
            variables['mensaje'] = "Guardado correctamente"
        except:
            variables['mensaje'] = "No se ha podido guardar"

    return render(request, 'core/tiendas.html',variables)

def detalleLista(request, id):
    lista = Lista.objects.filter(id_usuario=id)
    producto = Producto.objects.all()
    
    variables = {
       'list':lista,
       'product': producto
    }


    return render(request, 'core/agregar_producto.html',variables)

# def cargarProducto()
#     infoProduct = Producto.objects.filter(id=id)
#         print(infoProduct)

