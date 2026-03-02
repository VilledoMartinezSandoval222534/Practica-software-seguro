from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contactos, name='lista'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('editar/<int:id>/', views.editar_contacto, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_contacto, name='eliminar'),
]