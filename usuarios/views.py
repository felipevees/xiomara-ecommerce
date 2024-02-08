from django.shortcuts import render
from productos.models import Producto
from categorias.models import Categoria
from django.contrib.auth.decorators import login_required

def home(request):
    products = Producto.objects.all()
    categorias = Categoria.objects.all()
    # Pasar los objetos como contexto a la vista
    return render(request, 'home.html', {'products': products, 'categorias':categorias})

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def information(request):
    return render(request, 'information.html')