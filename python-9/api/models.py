from django.db import models
from django.core.validators import MinLengthValidator


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status', default=True)
    env = models.CharField('Env', max_length=50)
    version = models.CharField('Versão', max_length=5)
    address = models.GenericIPAddressField('Endereço IP', protocol='IPv4')

    class Meta:
        verbose_name_plural = 'Agentes'
        verbose_name = 'Agentes'

    def __str__(self):
        return self.name + ' | ' + self.env


class User(models.Model):

    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Ùltimo acesso', auto_now=True)
    email = models.EmailField('E-mail')
    password = models.CharField(
        'Senha',
        max_length=50,
        validators=[MinLengthValidator(8)]
    )

    class Meta:
        verbose_name_plural = 'Usuários'
        verbose_name = 'Usuário'

    def __str__(self):
        return self.name + ' ' + self.email


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name_plural = 'Grupos'
        verbose_name = 'Grupo'

    def __str__(self):
        return self.name


class Event(models.Model):

    CRITICAL = 'CRITICAL'
    DEBUG = 'DEBUG'
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'

    LEVEL_CHOICES = (
        (CRITICAL, CRITICAL),
        (DEBUG, DEBUG),
        (ERROR, ERROR),
        (WARNING, WARNING),
        (INFO, INFO),
    )

    level = models.CharField('Nível', max_length=20,
                             choices=LEVEL_CHOICES)

    data = models.TextField('Dados')
    arquivado = models.BooleanField('Arquivado', default=False)
    date = models.DateField('Data', null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Eventos'
        verbose_name = 'Evento'

    def __str__(self):
        return self.level


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Usuários do Grupo'
        verbose_name = 'Usuário do Grupo'

    def __str__(self):
        return self.group.name + ' ' + self.user.name