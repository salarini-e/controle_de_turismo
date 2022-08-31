# Generated by Django 4.0.6 on 2022-07-26 17:59

import contas.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0020_viagem_turismo_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viagem',
            name='cnpj_empresa_transporte',
            field=models.CharField(max_length=18, validators=[contas.functions.validate_CNPJ]),
        ),
    ]
