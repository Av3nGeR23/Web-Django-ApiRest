from operator import index
from django.shortcuts import render, redirect
from .forms import ProductoStockForm
from .models import ProductoStock
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from .models import ProductoStock
from django.contrib.auth.decorators import login_required


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoStockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Producto agregado correctamente!')
            return redirect('agregar_producto')  # Redirige a la misma página después de agregar un producto
    else:
        form = ProductoStockForm()

    productos = ProductoStock.objects.all()  # Obtener todos los productos existentes
    return render(request, 'agregar_producto.html', {'form': form, 'productos': productos})





@permission_required('Stock.puede_eliminar_producto', raise_exception=True)
def eliminarProyecto(request, id):
    producto = get_object_or_404(ProductoStock, pk=id)  # Obtener el producto basado en su ID
    if request.method == 'POST':
        producto.delete()  # Eliminar el producto
        return redirect('list_products')  # Redirigir a la lista de productos después de eliminar
    return render(request, 'agregar_producto.html', {'producto': producto})

@permission_required('Stock.puede_actualizar_producto', raise_exception=True)
def actualizarProyecto(request, id):
    producto = get_object_or_404(ProductoStock, pk=id)  # Obtener el producto basado en su ID
    form = ProductoStockForm(instance=producto)  # Crear un formulario con los datos del producto

    if request.method == 'POST':
        form = ProductoStockForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()  # Guardar los cambios en el producto
            return redirect('list_products')  # Redirigir a la lista de productos después de actualizar

    return render(request, 'agregar_producto.html', {'form': form})


