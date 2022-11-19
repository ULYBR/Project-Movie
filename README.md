# Pobrix - Plataforma de filmes 
Um projeto de uma plataforma de filmes inspirada na Netflix.
## Tecnologias usadas:
### Front-End:
- HTML5
- CSS3
- JavaScript
- TailwindCSS3
- Bootstrap5 (Django-Crispy-Forms)
### Back-End:
- Python
- Django
## Funcionalidades do site:

- Filme de destaque selecionado dinamicamente
- Lista de filmes novos gerada dinamicamente com base na data de adição do filme na plataforma
- Lista de filmes em alta gerada dinamicamente pelo número de vizualizações dos filmes
- Lista de filmes assistidos gerada dinamicamente
- Contabilização de vizualizações dinâmica
- Login
- Logout
- Edição de Perfil
- Edição de Senha
- Criação de novas contas

## Para instalação do App
```bash 

git init 

git clone https://github.com/ULYBR/Project-Movie.git

```

## Instalação do ambiente virtual

```bash

# criação do ambiente
  
  python -m venv venv

# inicialização do venv
  
  venv/scripts/venv
  
# instalação do requirements

  pip install -r requirements.txt


# inicialização do App

  python manage.py runserver

```

#APP irá abrir em um link localhost.

```bash
# Lembrando que terá que criar um superadmin do Django.

  
  python manage.py create superuser
  
 
 ```
 
 ## Logo após todos os passos é só adicionar os filmes que App está pronto.





