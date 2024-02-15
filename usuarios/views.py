from django.shortcuts import render, redirect

from productos.models import ImagenProducto, Producto
from categorias.models import Categoria

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login

from django.db.models import Q

def home(request):
    products = Producto.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'products': products, 'categorias':categorias})

#Login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth_login(request, user)
            return redirect('dashboard')  
        else:
           
            error_message = "Credenciales inválidas. Inténtelo de nuevo."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'registration/login.html')

#Dashboard

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

#Productos

def products(request):
    categorias = Categoria.objects.all()
    products = Producto.objects.all()
    return render(request, 'products.html', {'products': products, 'categorias': categorias})

def createProduct(request):
    nombreProducto = request.POST['nombre']
    descripcionProducto = request.POST['descripcion']
    short_descProducto = request.POST['short_desc']
    precioProducto = request.POST['precio']
    categorias_ids = request.POST.getlist('categorias')
    producto=Producto.objects.create(nombre=nombreProducto, descripcion=descripcionProducto, short_desc= short_descProducto, precio= precioProducto)
    producto.categorias.set(categorias_ids)
    producto.save()

    for imagen in request.FILES.getlist('imagenes'):
            ImagenProducto.objects.create(producto=producto, imagen=imagen)
    return redirect('products')

def deleteProduct(request, id):
    products = Producto.objects.get(id=id)
    products.delete()
    return redirect('products')

def updateProduct(request, id):
    productoActualizado = Producto.objects.get(id=id)
    nombreProductoActualizado = request.POST['nombre']
    descripcionProductoActualizado = request.POST['descripcion']
    short_descProductoActualizado = request.POST['short_desc']
    precioProductoActualizado = request.POST['precio']
    categorias_idsActualizado = request.POST.getlist('categorias')

    productoActualizado.nombre = nombreProductoActualizado
    productoActualizado.descripcion = descripcionProductoActualizado
    productoActualizado.short_desc = short_descProductoActualizado
    productoActualizado.precio = precioProductoActualizado
    
    productoActualizado.categorias.set(categorias_idsActualizado)
    productoActualizado.save()
    productoActualizado.imagenes.all().delete()
    for imagen in request.FILES.getlist('imagenes'):
        ImagenProducto.objects.create(producto=productoActualizado, imagen=imagen)
    return redirect('products')

#Categorias

def categories(request):
    categorias = Categoria.objects.all()
    return render(request, 'categories.html',{'categorias':categorias} )

def createCategory(request):
    nombreCategoria = request.POST['nombre']
    descripcionCategoria = request.POST['descripcion']
    categorias=Categoria(nombre=nombreCategoria, descripcion=descripcionCategoria)
    categorias.save()
    return redirect('categories')

def deleteCategory(request, id):
    categorias = Categoria.objects.get(id=id)
    categorias.delete()
    return redirect('categories')

def updateCategory(request, id):
    categorias = Categoria.objects.get(id=id)
    nombreActualizado = request.POST['nombre']
    descripcionActualizada = request.POST['descripcion']
    categorias.nombre=nombreActualizado
    categorias.descripcion=descripcionActualizada
    categorias.save()
    return redirect('categories')

#Information

def information(request):
    products = Producto.objects.all()
    return render(request, 'information.html', {'products': products})

#Search

def search(request):
    if request.method == "POST":
        searched = request.POST['searched'].lower()
        products = Producto.objects.filter(Q(nombre__icontains=searched) | Q(categorias__nombre__icontains=searched))
        return render(request, 'search.html', {'searched': searched, 'products':products})
    else:
        return render(request, 'search.html')