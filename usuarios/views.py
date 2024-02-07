from django.shortcuts import render
from productos.models import Producto
from categorias.models import Categoria

def home(request):
    products = Producto.objects.all()
    categorias = Categoria.objects.all()
    # Pasar los objetos como contexto a la vista
    return render(request, 'home.html', {'products': products, 'categorias':categorias})