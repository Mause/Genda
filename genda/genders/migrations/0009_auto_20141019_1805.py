# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genders', '0008_auto_20141019_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertopronoun',
            name='email_hash',
            field=models.CharField(max_length=32),
        ),
    ]
