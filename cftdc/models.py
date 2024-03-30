from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from setup.models import AuthUser

# Create your models here.

DIA_SEMANA = [
    ('0', 'Domingo'),
    ('1', 'Segunda'),
    ('2', 'Terça'),
    ('3', 'Quarta'),
    ('4', 'Quinta'),
    ('5', 'Sexta'),
    ('6', 'Sábado'),
]
HORA_DIA = [
    ('0', '00:00'), ('1', '00:30'), ('2', '01:00'), ('3', '01:30'), ('4', '02:00'), ('5', '02:30'),
    ('6', '03:00'), ('7', '03:30'), ('8', '04:00'), ('9', '04:30'), ('10', '05:00'), ('11', '05:30'),
    ('12', '06:00'), ('13', '06:30'), ('14', '07:00'), ('15', '07:30'), ('16', '08:00'), ('17', '08:30'),
    ('18', '09:00'), ('19', '09:30'), ('20', '10:00'), ('21', '10:30'), ('22', '11:00'), ('23', '11:30'),
    ('24', '12:00'), ('25', '12:30'), ('26', '13:00'), ('27', '13:30'), ('28', '14:00'), ('29', '14:30'),
    ('30', '15:00'), ('31', '15:30'), ('32', '16:00'), ('33', '16:30'), ('34', '17:00'), ('35', '17:30'),
    ('36', '18:00'), ('37', '18:30'), ('38', '19:00'), ('39', '19:30'), ('40', '20:00'), ('41', '20:30'),
    ('42', '21:00'), ('43', '21:30'), ('44', '22:00'), ('45', '22:30'), ('46', '23:00'), ('47', '23:30'),
]
STATUS_ALUNO = [
    ('ativo', 'Ativo'),
    ('inativo', 'Inativo'),
    ('pendencias', 'Pendencias'),
    ('inapto', 'Inapto')
]


class AlunoResponsavel(models.Model):
    nome = models.CharField(max_length=150, blank=True, null=True)

    def is_menor_idade(self):
        idade = timezone.now().year - self.data_nascimento.year
        return idade < 18

    @property
    def is_responsavel_required(self):
        return self.is_menor_idade()

    def __str__(self):
        return self.nome



class Aluno(models.Model):
    nome = models.CharField(max_length=80, null=False, unique=True)
    rg = models.CharField(max_length=15, null=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    responsavel = models.ManyToManyField(AlunoResponsavel, blank=True)

    def is_menor_idade(self):
        idade = timezone.now().year - self.data_nascimento.year
        return idade < 18

    @property
    def is_responsavel_required(self):
        return self.is_menor_idade()

    def __str__(self):
        return self.nome


class Email(models.Model):
    email = models.EmailField(max_length=255, unique=True)


class Aluno_Email(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True)


class Aluno_Responsavel_Email(models.Model):
    aluno_responsavel = models.ForeignKey(AlunoResponsavel, on_delete=models.CASCADE, null=True)
    email = models.ForeignKey(Email, on_delete=models.CASCADE, null=True, related_name='aluno_responsavel_email')


class Telefone(models.Model):
    numero = models.CharField(max_length=11, unique=True)
    is_principal = models.BooleanField(default=False, null=False, verbose_name="Principal")


class Aluno_Telefone(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE, null=True, related_name='aluno_telefone')


class Aluno_Responsavel_Telefone(models.Model):
    aluno_responsavel = models.ForeignKey(AlunoResponsavel, on_delete=models.CASCADE, null=True)
    telefone = models.ForeignKey(Telefone, on_delete=models.CASCADE, null=True,
                                 related_name='aluno_responsavel_telefone')


class Curso(models.Model):
    codigo = models.CharField(max_length=15, null=False, unique=True)
    nome = models.CharField(max_length=255, null=False, unique=True)
    descricao = models.CharField(max_length=255, null=False)
    valor_matricula = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Valor Matricula')
    valor_mensalidade = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                            verbose_name='Valor Mensalidade')
    carga_horaria = models.IntegerField(default=0, null=False, verbose_name='Carga Horária')
    data_criacao = models.DateField(auto_now=True, null=False, verbose_name='Data de Criacao')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    codigo = models.CharField(max_length=15, null=False, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=False)
    dia_semana = models.CharField(max_length=1, null=False, choices=DIA_SEMANA, default=0,
                                  verbose_name='Dia Semana')
    horario_inicio = models.CharField(max_length=5, null=False, choices=HORA_DIA, default=HORA_DIA[0],
                                      verbose_name='Horário Início')
    horario_fim = models.CharField(max_length=5, null=False, choices=HORA_DIA, default=HORA_DIA[0],
                                   verbose_name='Horário Fim')
    valor_matricula = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Valor Matricula')
    valor_mensalidade = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                            verbose_name='Valor Mensalidade')
    data_inicio = models.DateField(null=False, verbose_name='Data de Início')
    data_fim = models.DateField(null=False, verbose_name='Data de Termino')

    def __str__(self):
        return self


class Matricula(models.Model):
    codigo = models.CharField(max_length=20, null=False, unique=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=False)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=False)
    data_matricula = models.DateField(auto_now=True, null=False, verbose_name='Data matricula')
    valor_matricula = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Valor Matricula')
    valor_mensalidade = models.DecimalField(max_digits=10, decimal_places=2, default=0,
                                            verbose_name='Valor Mensalidade')
