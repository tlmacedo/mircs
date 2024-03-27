from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Aluno(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=80)
    rg = models.TextField(max_length=15)
    cpf = models.TextField(max_length=11)
    data_nascimento = models.DateField()
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    descricao = models.TextField(max_length=255, null=False)
    nomenclatura = models.TextField(max_length=80, null=False)
    carga_horaria = models.IntegerField(default=0, null=False)
    data_criacao = models.DateField(auto_now=True, null=False)

    def __str__(self):
        return self.nome
