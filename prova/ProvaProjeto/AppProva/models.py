from django.db import models

# Definição do modelo Produto
class Produto(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=1500)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fk_tipo = models.CharField(max_length=250)
    limiteadulto = models.DecimalField(max_digits=10, decimal_places=2)
    limitecri = models.DecimalField(max_digits=10, decimal_places=2)
    limitebebe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

# Definição do modelo Nivel
class Nivel(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

# Definição do modelo Usuario
class Usuario(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return self.nome

# Definição do modelo Reclamacao para associar Produto com Usuario e Nivel
class Reclamacao(models.Model):
    inicio = models.DateField()
    fim = models.DateField()
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.usuario.nome} - {self.nivel.nome}"
