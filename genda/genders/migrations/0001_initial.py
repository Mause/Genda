# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pronoun',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('object_word', models.CharField(max_length=10)),
                ('subject_word', models.CharField(max_length=10)),
                ('self_word', models.CharField(max_length=10)),
                ('owner_word', models.CharField(max_length=10)),
                ('gid', models.ForeignKey(to='genders.Gender', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
