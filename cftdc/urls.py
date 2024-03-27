from django.urls import path, include

from cftdc.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'aluno', AlunosViewSet, basename='alunos')
router.register(r'curso', CursosViewSet, basename='cursos')

urlpatterns = [

    path('', include(router.urls)),

]