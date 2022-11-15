from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class FormHome(forms.Form):
    email = forms.EmailField(label=False)


#criando formulario de criação de usuário padrão
class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    


    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')#criando personalizado requisitando email
