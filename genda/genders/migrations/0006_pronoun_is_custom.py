# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0005_usertopronoun_default_pronoun'),
    ]

    operations = [
        migrations.AddField(
            model_name='pronoun',
            name='is_custom',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
