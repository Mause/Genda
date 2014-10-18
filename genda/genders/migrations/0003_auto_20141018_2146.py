# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0002_auto_20141018_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='pronoun',
            name='name',
            field=models.CharField(max_length=20, default=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pronoun',
            name='gid',
        ),
    ]
