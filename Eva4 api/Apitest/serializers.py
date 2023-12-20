from rest_framework import serializers
from .models import ProductoStock

class ProductoStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoStock
        fields = '__all__' 
