# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-01 12:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('idBill', models.AutoField(db_column=b'idBill', primary_key=True, serialize=False, verbose_name=b'Factura')),
                ('total', models.DecimalField(db_column=b'total', decimal_places=2, default=0.0, help_text=b'1 a 7 parte entera, 2 parte decimal.', max_digits=9, validators=[django.core.validators.RegexValidator(code=b'invalid_total', message=b'1 a 7 parte entera y 2 parte decimal.', regex=b'^(([0-9]{1,7}\\.[0-9]{1,2})|([0-9]{1,7}))$')], verbose_name=b'Total')),
                ('date', models.CharField(db_column=b'date', default=b'2016-06-10', help_text=b'aaaa-mm-dd.', max_length=10, validators=[django.core.validators.RegexValidator(code=b'invalid_date', message=b'aaaa-mm-dd.', regex=b'^([2-9][0-9]{3})\\-(0[1-9]|1[0-2])\\-(0[1-9]|[1|2][0-9]|[3][0|1])$')], verbose_name=b'Fecha')),
            ],
            options={
                'db_table': 'Bill',
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('idLine', models.AutoField(db_column=b'idLine', primary_key=True, serialize=False, verbose_name=b'Linea')),
                ('price', models.DecimalField(db_column=b'price', decimal_places=2, default=0.0, help_text=b'1 a 5 parte entera, 2 parte decimal.', max_digits=7, validators=[django.core.validators.RegexValidator(code=b'invalid_price', message=b'1 a 5 parte entera y 2 parte decimal.', regex=b'^(([0-9]{1,5}\\.[0-9]{1,2})|([0-9]{1,5}))$')], verbose_name=b'Precio')),
                ('quantity', models.CharField(db_column=b'quantity', default=1, help_text=b'Minimo 1, maximo 99.', max_length=2, validators=[django.core.validators.RegexValidator(code=b'invalid_quantity', message=b'Entre 1 y 99.', regex=b'^([1-9]{1,1}|[1-9]{1,1}[0-9]{1,1})$')], verbose_name=b'Cantidad')),
                ('subtotal', models.DecimalField(db_column=b'subtotal', decimal_places=2, default=0.0, help_text=b'1 a 6 parte entera, 2 parte decimal.', max_digits=8, validators=[django.core.validators.RegexValidator(code=b'invalid_subtotal', message=b'1 a 6 parte entera y 2 parte decimal.', regex=b'^(([0-9]{1,6}\\.[0-9]{1,2})|([0-9]{1,6}))$')], verbose_name=b'Subtotal')),
            ],
            options={
                'db_table': 'Line',
                'verbose_name': 'Linea',
                'verbose_name_plural': 'Lineas',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('idProduct', models.AutoField(db_column=b'idProduct', primary_key=True, serialize=False, verbose_name=b'Producto')),
                ('name', models.CharField(db_column=b'name', default=b'', help_text=b'Solo letras, numeros y espacios.', max_length=200, unique=True, validators=[django.core.validators.RegexValidator(code=b'invalid_name', message=b'Solo letras, puntuacion y numeros, maximo 200.', regex=b'^([0-9a-zA-Z][, .:]*){1,200}$')], verbose_name=b'Nombre')),
                ('description', models.TextField(db_column=b'description', default=b'', help_text=b'Solo letras, numeros y espacios.', validators=[django.core.validators.RegexValidator(code=b'invalid_description', message=b'Solo letras, puntuacion y numeros, maximoa 500.', regex=b'^([0-9a-zA-Z][, .:]*){1,500}$')], verbose_name=b'Descripcion')),
                ('image', models.ImageField(db_column=b'image', help_text=b'jpg,bmp,svg o png.', upload_to=b'product/', verbose_name=b'Imagen')),
                ('price', models.DecimalField(db_column=b'price', decimal_places=2, default=0.0, help_text=b'1 a 3 parte entera, 2 parte decimal.', max_digits=5, validators=[django.core.validators.RegexValidator(code=b'invalid_price', message=b'1 a 3 parte entera y 2 parte decimal.', regex=b'^(([0-9]{1,3}\\.[0-9]{1,2})|([0-9]{1,3}))$')], verbose_name=b'Precio')),
            ],
            options={
                'db_table': 'Product',
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('idStock', models.AutoField(db_column=b'idStock', primary_key=True, serialize=False, verbose_name=b'Stock')),
                ('quantity', models.CharField(db_column=b'quantity', default=1, help_text=b'Minimo 1, maximo 99.', max_length=2, validators=[django.core.validators.RegexValidator(code=b'invalid_quantity', message=b'Entre 1 y 99.', regex=b'^([1-9]{1,1}|[1-9]{1,1}[0-9]{1,1})$')], verbose_name=b'Cantidad')),
                ('product', models.ForeignKey(db_column=b'product', on_delete=django.db.models.deletion.CASCADE, related_name='stock_product', to='product.Product', verbose_name=b'Producto')),
            ],
            options={
                'db_table': 'Stock',
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
            },
        ),
        migrations.AddField(
            model_name='line',
            name='product',
            field=models.ForeignKey(db_column=b'product', on_delete=django.db.models.deletion.CASCADE, related_name='line_product', to='product.Product', verbose_name=b'Producto'),
        ),
        migrations.AddField(
            model_name='bill',
            name='line',
            field=models.ForeignKey(db_column=b'line', on_delete=django.db.models.deletion.CASCADE, related_name='bill_line', to='product.Line', verbose_name=b'Linea'),
        ),
    ]
