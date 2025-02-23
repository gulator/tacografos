# Generated by Django 4.1.1 on 2024-12-06 11:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_vehiculo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca_vehiculo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dominio', models.CharField(max_length=10)),
                ('chasis', models.CharField(max_length=25)),
                ('marca_vehiculo', models.CharField(max_length=20)),
                ('modelo_vehiculo', models.CharField(max_length=20)),
                ('ano_vehiculo', models.IntegerField()),
                ('operador', models.CharField(max_length=30)),
                ('cuit', models.CharField(max_length=11)),
                ('marca_tacografo', models.CharField(max_length=20)),
                ('sn', models.CharField(max_length=26)),
                ('factor_k', models.CharField(max_length=6)),
                ('rodado', models.CharField(max_length=16)),
                ('limite_v', models.CharField(max_length=10)),
                ('fecha', models.DateField()),
                ('ot', models.CharField(max_length=30)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
