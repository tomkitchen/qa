# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=400)),
                ('answer', models.CharField(max_length=400)),
                ('chapter', models.CharField(max_length=10, choices=[(b'Chapter1', b'Chapter 1'), (b'Chapter2', b'Chapter 2'), (b'Chapter3', b'Chapter 3'), (b'Chapter4', b'Chapter 4'), (b'Chapter5', b'Chapter 5'), (b'Chapter6', b'Chapter 6'), (b'Chapter7', b'Chapter 7'), (b'Chapter8', b'Chapter 8'), (b'Chapter9', b'Chapter 9'), (b'Chapter10', b'Chapter 10'), (b'Chapter11', b'Chapter 11'), (b'Chapter12', b'Chapter 12'), (b'Chapter13', b'Chapter 13'), (b'Chapter14', b'Chapter 14'), (b'Chapter15', b'Chapter 15'), (b'Chapter16', b'Chapter 16'), (b'Chapter17', b'Chapter 17'), (b'Chapter18', b'Chapter 18'), (b'Chapter19', b'Chapter 19'), (b'Chapte20', b'Chapter 20'), (b'Chapter21', b'Chapter 21'), (b'Chapter22', b'Chapter 22')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
