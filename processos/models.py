from django.db import models


class Processo(models.Model):
    pasta = models.CharField('Pasta', max_length=100, blank=False)
    comarca = models.CharField('Comarca', max_length=50, blank=False)
    uf = models.CharField('UF', max_length=2, blank=False)

    class Meta:
        verbose_name = "Processo"
        verbose_name_plural = "Processos"

    def __str__(self):
        name = f"{self.pasta} - {self.comarca}-{self.uf}"
        return  name