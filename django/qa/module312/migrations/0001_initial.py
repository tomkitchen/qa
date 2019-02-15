# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module312Card',
            fields=[
                ('card_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flashcards.Card')),
            ],
            options={
            },
            bases=('flashcards.card',),
        ),
    ]
