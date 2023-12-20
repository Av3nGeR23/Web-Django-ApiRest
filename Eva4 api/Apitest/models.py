# En models.py de la app Stock

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
 

class ProductoStock(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    talla = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1)])
    cantidad_disponible = models.PositiveIntegerField(validators=[MinValueValidator(0)])

    class Meta:
        db_table = 'stock_productostock'

