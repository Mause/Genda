# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pronoun',
            name='gid',
            field=models.ForeignKey(blank=True, null=True, to='genders.Gender'),
        ),
    ]
