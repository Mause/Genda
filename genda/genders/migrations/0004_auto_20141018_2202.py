# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('genders', '0003_auto_20141018_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToPronoun',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('email_hash', models.CharField(max_length=30)),
                ('user', models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='pronoun',
            name='name',
        ),
    ]
