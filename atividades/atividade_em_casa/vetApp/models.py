from django.db import models

# Create your models here.

class pet(models.Model):
    nome = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    

class Anaminese(models.Model):

    pet = models.ForeignKey(pet, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Mete:

        verbose_name_plural = "Anaminesese"

    def __str__(self):
        return self.text[:50] + '...'