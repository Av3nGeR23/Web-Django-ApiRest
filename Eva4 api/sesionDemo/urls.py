 
from django.contrib import admin
from django.urls import include, path
from sesionApp import views  
from django.contrib.auth.views import LoginView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('products/', views.list_products, name='list_products'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('', include('sesionApp.urls')),   
    path('stock/', include('Stock.urls')),
    path('place_order/', views.place_order, name='place_order'),
    path('api', include('Apitest.urls')),
    path('docs/',include_docs_urls(title= 'Api Documentacion'))
]