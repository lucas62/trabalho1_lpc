from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=100,null=True, blank=False)
    usuario = models.ForeignKey(User,null=True, blank=False)

    def __str__(self):
        return self.nome

class PessoaJuridica(Pessoa):
    cnpj = models.CharField(max_length=24,null=True,blank=False)
    razaoSocial = models.CharField(max_length=100, null=True,blank=False)

class PessoaFisica(Pessoa):
    cpf = models.CharField(max_length=11,null=True,blank=False)

class Autor(Pessoa):
    curriculo = models.TextField(max_length=500,null=True,blank=False)

class Evento(models.Model):
    nome = models.CharField(max_length=150,null=True,blank=False)
    eventoPrincipal = models.CharField(max_length=150,null=True,blank=False)
    sigla = models.CharField(max_length=5,null=True,blank=False)
    dataEHoraDeInicio = models.DatetimeField(blank=False,null=True)
    palavrasChaves = models.CharField(max_length=150,null=True,blank=False)
    logotipo = models.CharField(max_length=150, null=True,blank=False)
    realizador = models.ForeignKey(Pessoa,null=True,blank=False)
    cidade = models.CharField(max_length=100, null=True,blank=False)
    uf = models.CharField(max_length=2,null=True,blank=False)
    endereco = models.CharField(max_length=200,null=True,blank=False)
    cep = models.CharField(max_length=8,null=True,blank=False)

    def __str__(self):
        return '{} - {}'.format(self.nome, self.realizador.nome)

class EventoCientifico(Evento):
    issn = models.CharField(max_length=100,null=True,blank=False)

class ArtigoCientifico(models.Model):
    titulo = models.CharField(max_length=150,null=True,blank=False)
    autores = models.CharField(max_length=500,null=True)
    evento = models.ForeignKey(EventoCientifico,null=True,blank=False)