# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 13:16
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column=b'name', default=b'', help_text=b'Solo letras, numeros y espacios.', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_name', message=b'Solo letras, puntuacion y numeros, maximo 200.', regex=b'^([0-9a-zA-Z][, .:]*){1,200}$')], verbose_name=b'Nombre')),
                ('dni', models.CharField(db_column=b'dni', help_text=b'8 numeros, guion y letra.', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_name', message=b'Solo letras, puntuacion y numeros, maximo 200.', regex=b'^([0-9]{8}-[A-Z]{1,1})$')], verbose_name=b'DNI')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'UserApp',
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
