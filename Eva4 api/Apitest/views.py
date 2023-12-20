
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, render, redirect
from .models import ProductoStock
from .serializers import ProductoStockSerializer
from django.contrib.auth.decorators import permission_required
from .permissions import SuperAdminOnly

class ProductoStockViewSet(viewsets.ModelViewSet):
    queryset = ProductoStock.objects.all()
    serializer_class = ProductoStockSerializer
    permission_classes = [SuperAdminOnly]

