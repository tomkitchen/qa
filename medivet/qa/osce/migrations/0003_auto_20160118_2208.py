# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osce', '0002_auto_20160118_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='station',
            field=models.CharField(max_length=100, choices=[(b'1', b'Nursing Care 1 Fluid Therapy')]),
            preserve_default=True,
        ),
    ]
