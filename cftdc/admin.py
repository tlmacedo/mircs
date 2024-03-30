from django.contrib import admin
from cftdc.models import Aluno, Curso, Turma


# Register your models here.

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento', 'user')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'user',)
    list_per_page = 50


admin.site.register(Aluno, AlunosAdmin)


class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nome', 'descricao', 'carga_horaria', 'data_criacao')
    list_display_links = ('id', 'codigo', 'nome',)
    search_fields = ('id', 'codigo', 'nome', 'descricao')
    list_per_page = 20


admin.site.register(Curso, CursosAdmin)


class TurmasAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'codigo', 'curso', 'dia_semana', 'horario_inicio', 'horario_fim', 'valor_matricula', 'valor_mensalidade',
        'data_inicio', 'data_fim')
    list_display_links = ('id', 'codigo', 'curso')
    search_fields = ('id', 'codigo', 'curso')
    list_per_page = 50


admin.site.register(Turma, TurmasAdmin)
