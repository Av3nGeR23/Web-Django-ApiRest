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

    def clean(self):
        # Validación para el campo 'color'
        if not self.color.isalpha():
            raise ValidationError({'color': 'El color debe contener solo letras'})

        # Validación para el campo 'precio'
        if not str(self.precio).replace('.', '', 1).isdigit():
            raise ValidationError({'precio': 'El precio debe contener solo números'})

        # Validación para el campo 'cantidad_disponible'
        if not str(self.cantidad_disponible).isdigit():
            raise ValidationError({'cantidad_disponible': 'La cantidad disponible debe contener solo números'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Llamar a full_clean() para ejecutar las validaciones
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.marca} - {self.modelo} - Talla: {self.talla} - Color: {self.color}"
    class Meta:
        permissions = [
            ("puede_eliminar_producto", "Puede eliminar productos"),
            ("puede_actualizar_producto", "Puede actualizar productos"),
        ]

       