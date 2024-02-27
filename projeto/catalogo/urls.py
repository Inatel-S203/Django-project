from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.listar_filmes, name='listar_filmes'),
    path('', views.listar_filmes, name='home'),  # Adiciona esta linha
]
