from rest_framework import serializers

from cftdc.models import Aluno, Curso, Turma


class AlunoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Aluno
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        exclude = []


class ListaCursoTurmasSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.nome')
    descricao = serializers.ReadOnlyField(source='curso.descricao')

    class Meta:
        model = Turma
        fields = ['curso', 'descricao', 'nomenclatura', 'data_inicio']
