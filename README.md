# Guia para Executar sua Aplicação Django e Adicionar Filmes

Este guia passo a passo ensina como executar sua aplicação Django usando o `runserver` e como adicionar novos filmes ao banco de dados programaticamente.

## Rodando a Aplicação Django

### Passo 1: Ativando o Ambiente Virtual

Antes de iniciar sua aplicação, é recomendado ativar o ambiente virtual do Python para isolar as dependências do projeto. Abra o terminal ou prompt de comando e navegue até o diretório do seu projeto Django. Ative o ambiente virtual com um dos seguintes comandos:

**Para Windows:**

``\path\to\env\Scripts\activate``

**Para Unix ou MacOS:**

``source /path/to/env/bin/activate``


### Passo 2: Executando o Servidor de Desenvolvimento  

Com o ambiente virtual ativado, execute o servidor de desenvolvimento do Django com o comando:

``python manage.py runserver``

Após iniciar o servidor, você pode acessar a aplicação abrindo http://127.0.0.1:8000/ no seu navegador.


## Adicionando um Novo Filme Programaticamente

### Passo 1: Abrindo o Shell do Django

Para adicionar um novo filme diretamente no banco de dados, você usará o shell interativo do Django. Com o ambiente virtual ainda ativado, abra o shell com o comando:  

``python manage.py shell``


### Passo 2: Importando o Modelo Filme

No shell do Django, importe o modelo Filme do seu aplicativo. Substitua catalogo pelo nome do seu aplicativo Django, se for diferente:

``from catalogo.models import Filme``


### Passo 3: Criando e Salvando um Novo Filme  

Crie uma nova instância do modelo Filme, preenchendo os campos necessários. Por exemplo, para adicionar o novo filme:

``from catalogo.models import Filme`` -> Para importar  novamente o modelo

``novo_filme = Filme(
    titulo="nome_filme", 
    ano_de_lancamento=ano_filme,
    diretor="diretor_filme",
    genero="genero_filme",
    duracao=duracao_min_filme  
)``

Salve a nova instância no banco de dados usando o método .save():  

``novo_filme.save()``


Após executar esses comandos, o novo filme será adicionado ao banco de dados do seu projeto Django.


### Passo 4: Encerrando o Shell  

Quando terminar de adicionar filmes, você pode sair do shell do Django digitando ``exit()`` ou pressionando Ctrl+D.

