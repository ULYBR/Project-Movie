from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.



# lista de categorias 
LISTA_CATEGORIAS = (
    ("Acao", "Ação"),
    ("Anime", "Anime"),
    ("Aventura", "Aventura"),
    ("Comedia", "Comédia"),
    ("Documentario", "Documentário"),
    ("Infantil", "Infantil"),
    ("Romance", "Romance"),
    ("Terror", "Terror"),
    ("Drama","Drama"),
    )
# modelo de filme
class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumbs-filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=16, choices=LISTA_CATEGORIAS)
    visualizacoes = models.IntegerField(default=0)
    data_criacao = models.DateTimeField(default=timezone.now)

# funcao de mostra o nome do filme 
    def __str__(self):
        return self.titulo






#Criar episódio

class Episodio(models.Model):
    filme = models.ForeignKey("Filme", related_name="episodios", on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    video = models.URLField()
    
    # funcao de mostra o nome do episodio
    def __str__(self):
        return self.filme.titulo + " - " + self.titulo
    


#Criar usuário 


class Usuario(AbstractUser):
    filmes_vistos = models.ManyToManyField("Filme")
    
    