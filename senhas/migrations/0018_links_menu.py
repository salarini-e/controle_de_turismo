# Generated by Django 3.2.15 on 2022-10-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senhas', '0017_viagem_turismo_telefone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links_Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=120)),
                ('url', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
