# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0006_pronoun_is_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertopronoun',
            name='default_gender',
            field=models.ForeignKey(
                to='genders.Gender', null=True
            ),
            preserve_default=False,
        ),
    ]
