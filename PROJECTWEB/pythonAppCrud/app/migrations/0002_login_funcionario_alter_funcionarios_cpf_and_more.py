# Generated by Django 5.1.2 on 2024-10-15 13:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.funcionarios'),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='cpf',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^\\d{11}$', 'O CPF deve ter 11 dígitos numéricos.')]),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='email',
            field=models.EmailField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
