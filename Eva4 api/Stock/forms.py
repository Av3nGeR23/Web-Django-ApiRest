# En forms.py de la app Stock

from django import forms
from .models import ProductoStock

class ProductoStockForm(forms.ModelForm):
    class Meta:
        model = ProductoStock
        fields = ['marca', 'modelo', 'talla', 'color', 'precio', 'cantidad_disponible']
