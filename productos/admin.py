# admin.py

from django import forms
from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, ImagenProducto

class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto

class ProductoAdminForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoAdminForm
    inlines = [ImagenProductoInline]

admin.site.register(Producto, ProductoAdmin)
