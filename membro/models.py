from django.db import models


# Create your models here.

class Membro(models.Model):
    FUNCAO = [
        ('', ''),
        ('A', 'Apóstolo'),
        ('P', 'Pastor'),
        ('L', 'Líder de Célula'),
        ('D', 'Discípulo'),
        ('M', 'Membro'),
    ]
    nome = models.CharField(max_length=150, blank=False, null=False)
    apelido = models.CharField(max_length=30, blank=False, null=False)
    funcao = models.CharField(max_length=1, choices=FUNCAO, default='M')

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=150, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    complemento = models.CharField(max_length=60, blank=True)
    bairro = models.CharField(max_length=50, blank=False, null=False)
    ponto_de_referencia = models.CharField(max_length=80, blank=False, null=False)
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)

    def __str__(self):
        return self.logradouro


class MembroEndereco(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)


class Uf(models.Model):
    descricao = models.CharField(max_length=80, blank=False, null=False)
    sigla = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return self.sigla


class Municipio(models.Model):
    descricao = models.CharField(max_length=120, blank=False, null=False)
    capital = models.BooleanField(default=False)
    ibge_codigo = models.CharField(max_length=7, blank=False, null=False)
    ddd = models.IntegerField()
    uf = models.ForeignKey(Uf, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class Telefone(models.Model):
    descricao = models.CharField(max_length=11, blank=False, null=False)
    principal = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao


class MembroTelefone(models.Model):
    membro = models.ForeignKey(Membro, on_delete=models.CASCADE)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE)
