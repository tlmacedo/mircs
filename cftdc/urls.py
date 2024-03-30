from django.urls import path, include

from cftdc.views import AlunosViewSet, CursosViewSet, TurmaViewSet, ListaCursoTurmas
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'cursos', CursosViewSet, basename='Cursos')
router.register(r'turmas', TurmaViewSet, basename='Turmas')

urlpatterns = [

    path('', include(router.urls)),
    path('curso/<int:pk>/turmas/', ListaCursoTurmas.as_view(), name='lista_curso_turmas')

]
