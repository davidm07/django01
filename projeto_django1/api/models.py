from django.db import models

# Create your models here.
class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    ano_publicacao = models.DateField()


    def __str__(self) -> str:
        return self.nome
    
    