# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-03-23 11:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='Comentario',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='Nombre',
            new_name='nombre',
        ),
    ]
