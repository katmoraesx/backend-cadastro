# Generated by Django 5.1.5 on 2025-01-20 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ni', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('cel', models.CharField(max_length=255)),
                ('ocup', models.FloatField(max_length=255)),
            ],
        ),
    ]
