from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL para la lista de publicaciones
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # URL para los detalles de la publicación
]
