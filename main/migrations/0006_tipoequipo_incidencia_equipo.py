# Generated by Django 5.0.4 on 2024-05-06 16:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_configure'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solicita', models.CharField(max_length=100)),
                ('solicitante', models.CharField(max_length=100)),
                ('codSolicitante', models.IntegerField()),
                ('cargoUsuario', models.CharField(max_length=100)),
                ('solicitaConDoc', models.BooleanField(default=False)),
                ('nroDoc', models.CharField(blank=True, max_length=400, null=True)),
                ('fechaSolicita', models.DateTimeField(auto_now_add=True)),
                ('dejaEquipo', models.BooleanField(default=False)),
                ('fechaTermina', models.DateTimeField(null=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.area')),
                ('oficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.oficina')),
                ('userTic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('codPatrimonial', models.CharField(max_length=20)),
                ('descripcionEquipo', models.TextField(blank=True)),
                ('descripcionCompra', models.TextField(blank=True)),
                ('estadoPatrimonio', models.CharField(max_length=1)),
                ('responsablePatri', models.CharField(max_length=100)),
                ('oficinaPatri', models.CharField(max_length=100)),
                ('fechaUpdate', models.DateTimeField(null=True)),
                ('tipoEquipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tipoequipo')),
            ],
        ),
    ]
