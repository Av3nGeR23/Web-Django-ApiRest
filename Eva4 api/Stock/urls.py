# En urls.py de la app Stock

from django.urls import path
from . import views
 
urlpatterns = [
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('eliminar/<int:id>/', views.eliminarProyecto, name='eliminarProyecto'),
    path('actualizar/<int:id>/', views.actualizarProyecto, name='actualizarProyecto'),

]
