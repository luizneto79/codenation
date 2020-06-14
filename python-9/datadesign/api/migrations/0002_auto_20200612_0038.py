# Generated by Django 3.0.7 on 2020-06-12 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.GenericIPAddressField(verbose_name='Endereço IP'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='env',
            field=models.CharField(max_length=50, verbose_name='Env'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='version',
            field=models.CharField(max_length=5, verbose_name='Versão'),
        ),
        migrations.AlterField(
            model_name='event',
            name='arquivado',
            field=models.BooleanField(default=False, verbose_name='Arquivado'),
        ),
        migrations.AlterField(
            model_name='event',
            name='data',
            field=models.TextField(verbose_name='Dados'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='event',
            name='level',
            field=models.CharField(max_length=20, verbose_name='Nível'),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ùltimo acesso'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, verbose_name='Senah'),
        ),
    ]