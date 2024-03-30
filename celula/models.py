from django.db import models


# Create your models here.

class Celula(models.Model):
    nome = models.CharField(max_length=150)
