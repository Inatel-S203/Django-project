from django.shortcuts import render
from .models import Filme

def listar_filmes(request):
    filmes = Filme.objects.all()

    ano = request.GET.get('ano')
    if ano:
        filmes = filmes.filter(ano_de_lancamento=ano)

    genero = request.GET.get('genero')
    if genero:
        filmes = filmes.filter(genero__icontains=genero)

    diretor = request.GET.get('diretor')
    if diretor:
        filmes = filmes.filter(diretor__icontains=diretor)

    return render(request, 'catalogo/lista_filmes.html', {'filmes': filmes})

