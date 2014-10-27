from django.db import models
from django.conf import settings


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    __repr__ = __str__


class UserToPronoun(models.Model):
    email_hash = models.CharField(max_length=32)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)

    default_pronoun = models.ForeignKey('Pronoun')


class Pronoun(models.Model):
    object_word = models.CharField(max_length=10)  # them
    subject_word = models.CharField(max_length=10)   # they
    self_word = models.CharField(max_length=10)  # themself
    owner_word = models.CharField(max_length=10)  # their

    def __str__(self):
        return '{}/{}/{}/{}'.format(
            self.object_word,
            self.subject_word,
            self.self_word,
            self.owner_word
        )

    __repr__ = __str__
