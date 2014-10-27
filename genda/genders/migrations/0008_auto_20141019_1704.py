# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0007_usertopronoun_default_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertopronoun',
            name='default_gender',
            field=models.ForeignKey(to='genders.Gender', null=True),
        ),
    ]
