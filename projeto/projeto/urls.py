from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filmes/', include('catalogo.urls')),  # Supondo que 'catalogo.urls' tenha a view 'listar_filmes'
    path('', include('catalogo.urls')),  # Adicione esta linha para incluir as URLs do app 'catalogo' na raiz
]
