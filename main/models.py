from django.db import models
from tkinter import CASCADE
from django.db import models
 
# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    endereco = models.CharField(max_length=25)
 
class Categoria(models.Model):
    nome = models.CharField(max_length=25)
 
class Filme(models.Model):
    titulo = models.CharField(max_length=25)
    ano_lancamento= models.DateTimeField()
    valor_locacao = models.DecimalField(max_digits=4,decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
 
class Locacao(models.Model):
    data_entrega = models.DateTimeField()
    data_locacao = models.DateTimeField()
    valor = models.DecimalField(max_digits=4,decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filme = models.ManyToManyField(Filme, through='LocacaoFilme')
 
class LocacaoFilme(models.Model):
    filme = models.ForeignKey(Filme,models.CASCADE)
    Locacao = models.ForeignKey(Locacao,models.CASCADE)
 
 
 
