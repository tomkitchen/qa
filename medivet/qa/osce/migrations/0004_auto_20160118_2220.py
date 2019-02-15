# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('osce', '0003_auto_20160118_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='station',
            field=models.CharField(max_length=100, choices=[(b'1', b'Nursing Care 1 Fluid Therapy'), (b'2', b'Nursing Care 3 IM Injection')]),
            preserve_default=True,
        ),
    ]
