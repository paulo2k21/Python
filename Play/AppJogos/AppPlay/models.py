from django.db import models

# Create your models here.
class Jogos (models.Model):

    nome = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=1500)
    imagem = models.CharField(max_length=250)
    categoria = models.ForeignKey("Categoria",on_delete=models.CASCADE, null=True)
     
    def __str__(self):
        return self.nome
    
class Categoria (models.Model):
     nome = models.CharField(max_length=250)
     def __str__(self):
        return self.nome