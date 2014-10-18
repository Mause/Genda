# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0004_auto_20141018_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertopronoun',
            name='default_pronoun',
            field=models.ForeignKey(to='genders.Pronoun', default=None),
            preserve_default=False,
        ),
    ]
