"""acta_sports URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# urls.py

from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import home, login, dashboard, information, products,createProduct, categories, createCategory, deleteCategory, updateCategory

# ... tus otras URLpatterns

urlpatterns = [
    path("", home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('information/', information, name='information'),
    path('products/', products, name='products'),
    path('createProduct/', createProduct, name='createProduct'),
    path('categories/', categories, name='categories'),
    path('create_category/', createCategory, name='createCategory'),
    path('deleteCategory/<int:id>/', deleteCategory, name='deleteCategory'),
    path('updateCategory/<int:id>/', updateCategory, name="updateCategory"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



