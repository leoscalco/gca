# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-24 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0005_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producttype',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestao.ProductSize'),
        ),
        migrations.AlterField(
            model_name='document',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(default='', max_length=120),
        ),
    ]
