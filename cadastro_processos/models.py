from django.db import models


class Planilha(models.Model):
    nome = models.CharField(max_length=80, blank=False)
    cliente = models.CharField(max_length=80, blank=False)
    arquivo = models.FileField()
