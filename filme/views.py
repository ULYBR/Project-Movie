from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHome


# Create your views here.
#função que faz a requisição e retorna home.html FBV
#def homepage(request):
#   return render(request, "home.html" )

# metodo de classe irá usa um views pre feita do generic e quando é usado TemplateView é só para mostra um template listview irá mostra uma lista do model.
class Homepage(FormView): 
    template_name = "home.html"
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')

        else:

            return super().get(request, *args, **kwargs)
    #função de acordo com email que usuário coloca no imput da homepage ele redireciona o url .
    def get_success_url(self):
        email = self.request.POST.get("email")
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')    


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    #object_list vez de retorna list_filmes

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    
    #função para contabilizar uma visualização.
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1 # somo a visualizacao.
        filme.save() # salvar a mudança no banco de dados.
        usuario = request.user
        usuario.filmes_vistos.add(filme) # irá adicionar os filmes visto pelo usuario e irá contalibizar no bd.


        return super().get(request, *args, **kwargs) #redireciona o usuario para url final. 

    
    # DetailsView irá criar 1 item para cada modelo
    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        #filtrar a minha tabela de filmes pegando a categoria dos filmes para virar um filme relacionados .
        
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme
    #editando object_list
    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = self.model.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else:
            
            return None


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = "editarperfil.html"
    model = Usuario
    fields = ['first_name', 'last_name', 'email']
    
    def get_success_url(self):
        
        return reverse('filme:homefilmes')

class Criarconta(FormView):
    template_name = "criarconta.html"
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    #se a requisição for um sucesso ele retornara o link do filme:login
    def get_success_url(self):
        return reverse('filme:login')


class Videofilme(LoginRequiredMixin, DetailView):
    template_name = "video.html"
    model = Filme

    def get_success_url(self):
        return redirect('filme:video')

    

