from django.db import models
from django.conf import settings


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    __repr__ = lambda self: '<{}>'.format(self.__str__())


class UserToPronoun(models.Model):
    email_hash = models.CharField(max_length=32)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)

    default_pronoun = models.ForeignKey('Pronoun')
    default_gender = models.ForeignKey('Gender', null=True)

    def __str__(self):
        return '<{} prefers {}>'.format(
            self.user.username, self.default_pronoun
        )

    __repr__ = __str__


class Pronoun(models.Model):
    object_word = models.CharField(max_length=10)  # them
    subject_word = models.CharField(max_length=10)   # they
    self_word = models.CharField(max_length=10)  # themself
    owner_word = models.CharField(max_length=10)  # their

    is_custom = models.BooleanField(default=True)

    def __str__(self):
        return '{}/{}/{}/{}'.format(
            self.object_word,
            self.subject_word,
            self.self_word,
            self.owner_word
        )

    __repr__ = lambda self: '<{}>'.format(self.__str__())
