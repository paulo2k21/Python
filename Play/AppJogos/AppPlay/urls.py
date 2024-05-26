from django.urls import path
from django.urls import path, include
from AppPlay import views
from .views import *

urlpatterns = [
   
    path('', views.home, name='home'),
    path('jogo/<id_jogos>', views.jogos, name='jogos'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('form_jogos/', views.form_jogos, name ='form_jogos'),
    path('cadastrar_usuario', cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario/', logar_usuario, name="logar_usuario"),
    path('logout/', views.logout_view, name='logout')
    
]