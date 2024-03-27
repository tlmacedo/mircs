from django.http import JsonResponse

from rest_framework import viewsets

from cftdc.models import Aluno, Curso
from cftdc.serializer import AlunoSerializer, CursoSerializer


# Create your views here.


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer



class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
