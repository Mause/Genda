from django.db import models


class Gender(models.Model):
    # gid integer primary key autoincrement,
    name = models.CharField(max_length=20)



class Pronoun(models.Model):
    object_word = models.CharField(max_length=10)  # them
    subject_word = models.CharField(max_length=10)   # they
    self_word = models.CharField(max_length=10)  # themself
    owner_word = models.CharField(max_length=10)  # their
