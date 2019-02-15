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
                ('station', models.CharField(max_length=100, choices=[(b'1', b'Nursing Care 1 Fluid Therapy')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
