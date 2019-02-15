# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccnp', '0002_auto_20150620_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='chapter',
            field=models.CharField(max_length=100, choices=[(b'1', b'Chapter 1: Enterprise Campus Network Design'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6'), (b'7', b'7'), (b'8', b'8'), (b'9', b'9'), (b'10', b'10'), (b'11', b'11'), (b'12', b'12'), (b'13', b'13'), (b'14', b'14'), (b'15', b'15'), (b'16', b'16'), (b'17', b'17'), (b'18', b'18'), (b'19', b'19'), (b'20', b'20'), (b'21', b'21'), (b'22', b'22')]),
            preserve_default=True,
        ),
    ]
