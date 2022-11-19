


from django.urls import include, path, reverse_lazy

from .views import Detalhesfilme, Homefilmes, Homepage, Pesquisafilme, Paginaperfil, Criarconta, Videofilme
from django.contrib.auth import views as auth_view


app_name = "filme"


urlpatterns = [
    path('', Homepage.as_view(), name="home"),
    path('filmes/', Homefilmes.as_view(), name="homefilmes"),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', Pesquisafilme.as_view(), name="pesquisafilme"),
    path('login/', auth_view.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('editarperfil/<int:pk>', Paginaperfil.as_view(), name="editarperfil"),
    path('criarconta/', Criarconta.as_view(), name="criarconta"),
    path('mudarsenha/<int:pk>', auth_view.PasswordChangeView.as_view(template_name='editarperfil.html',
                                                             success_url=reverse_lazy('filme:homefilme')), name="mudarsenha"),
    path('video/<int:pk>', Videofilme.as_view(), name="video")
] 