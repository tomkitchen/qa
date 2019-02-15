# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='answer',
            field=models.CharField(max_length=400),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='card',
            name='question',
            field=models.CharField(max_length=400),
            preserve_default=True,
        ),
    ]
