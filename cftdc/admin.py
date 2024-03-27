from django.contrib import admin
from cftdc.models import Aluno, Curso


# Register your models here.

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'user',)
    list_per_page = 50


admin.site.register(Aluno, Alunos)


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'nomenclatura', 'carga_horaria', 'data_criacao')
    list_display_links = ('id', 'nome', 'nomenclatura')
    search_fields = ('id', 'nome', 'descricao', 'nomenclatura')
    list_per_page = 20


admin.site.register(Curso, Cursos)
