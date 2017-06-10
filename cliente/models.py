# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    email = models.EmailField()
    filhos = models.IntegerField()
    ativo = models.NullBooleanField()


    def __str__(self):
        return self.nome