from django.db import models
from django.conf import settings


class Gender(models.Model):
    # gid integer primary key autoincrement,
    name = models.CharField(max_length=20)


class UserToPronoun(models.Model):
    email_hash = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)

    default_pronoun = models.ForeignKey('Pronoun')


class Pronoun(models.Model):
    object_word = models.CharField(max_length=10)  # them
    subject_word = models.CharField(max_length=10)   # they
    self_word = models.CharField(max_length=10)  # themself
    owner_word = models.CharField(max_length=10)  # their
