from django.urls import path,include
from rest_framework import routers
from Apitest import views

router = routers.DefaultRouter()
router.register(r'ProductoStock',views.ProductoStockViewSet)


urlpatterns = [
    path('', include(router.urls))
    # Define otras rutas para actualización, eliminación, etc. si es necesario
]
