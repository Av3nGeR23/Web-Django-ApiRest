from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from .models import Producto
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Stock.models import ProductoStock
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Usuario {username} creado con éxito.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña no válidos')
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def view_cart(request):
    cart_key = f'cart_{request.user.id}'
    cart = request.session.get(cart_key, {})
    products_in_cart = {}
    
    for product_id, quantity in cart.items():
        try:
            product = ProductoStock.objects.get(pk=product_id)
            products_in_cart[product] = quantity
        except ProductoStock.DoesNotExist:
          
            pass  

    return render(request, 'view_cart.html', {'cart': products_in_cart})

@login_required
def clear_cart(request):
    cart_key = f'cart_{request.user.id}'
    if cart_key in request.session:
        del request.session[cart_key]
    return redirect('view_cart')

def list_products(request):
    products = ProductoStock.objects.all()
    return render(request, 'list_products.html', {'products': products})

@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    cart_key = f'cart_{request.user.id}'
    cart = request.session.get(cart_key, {})
    product = ProductoStock.objects.get(pk=product_id)

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        # Verificar si hay suficiente stock antes de agregar al carrito
        if product.cantidad_disponible > 0:
            cart[str(product_id)] = 1
            product.cantidad_disponible -= 1  # Restar una unidad del stock disponible
            product.save()
        else:
            messages.warning(request, f'No hay suficiente stock de {product.marca} {product.modelo} en talla {product.talla} y color {product.color}')

    request.session[cart_key] = cart
    return redirect('list_products')


@login_required
def place_order(request):
    cart_key = f'cart_{request.user.id}'
    cart = request.session.get(cart_key, {})
   
    return redirect('home')  # Redirige a la página de inicio después de realizar el pedido

