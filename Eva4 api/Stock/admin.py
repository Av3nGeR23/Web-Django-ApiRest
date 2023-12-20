from django.contrib import admin
from .models import ProductoStock

class ProductoStockAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'talla', 'color', 'precio', 'cantidad_disponible')
    search_fields = ('marca', 'modelo', 'talla', 'color')
    list_filter = ('marca', 'talla', 'color')
    readonly_fields = ('cantidad_disponible',)   

    def save_model(self, request, obj, form, change):
        # Aquí puedes realizar acciones adicionales antes de guardar el objeto
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        # Acciones adicionales al eliminar un objeto
        super().delete_model(request, obj)

admin.site.register(ProductoStock, ProductoStockAdmin)
