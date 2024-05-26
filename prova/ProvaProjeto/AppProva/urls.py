from django.urls import path
from AppProva import views
from AppProva.views import reclamacao_list

urlpatterns = [
   
   
     path(' ', reclamacao_list)
   
    
]