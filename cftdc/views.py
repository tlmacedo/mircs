from django.http import JsonResponse

from rest_framework import viewsets, generics

from cftdc.models import Aluno, Curso, Turma
from cftdc.serializer import AlunoSerializer, CursoSerializer, TurmaSerializer, ListaCursoTurmasSerializer


# Create your views here.


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as turmas """
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class ListaCursoTurmas(generics.ListAPIView):
    """Listando todas as turmas de um aluno"""
    def get_queryset(self):
        queryset = Turma.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaCursoTurmasSerializer