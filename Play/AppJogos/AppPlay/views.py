from multiprocessing import AuthenticationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from AppPlay.models import Jogos
from AppPlay.forms import JogosForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as authLogin, authenticate, login, logout

from django.contrib import auth
# Create your views here.

def home (request):
    jogos = Jogos.objects.order_by
    context = {'jogos':jogos}
    return render(request, 'index.html', context)


def jogos (request,id_jogos):
    jogos = Jogos.objects.get(id=id_jogos)                                   
    context = {'jogos':jogos}
    return render(request, 'jogos.html', context)

      
def contato (request):
    return render(request, 'contato.html')

def sobre (request):
    return render(request, 'sobre.html')

def form_jogos(request):
    """Adiciona um novo produto"""
    form = JogosForm()
   
    if request.method == 'POST':
            form = JogosForm(request.POST)

            if form.is_valid():
                form.save()
                form = JogosForm()  

    context = {'form': form}
    return render (request, 'formulario_jogos.html', context)


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('cadastrar_usuario')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})




def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('logar_usuario')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'login.html', {'form_login': form_login})

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(reverse('home')) 









