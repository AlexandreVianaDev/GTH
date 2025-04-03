from django.db import models


class Sexo(models.TextChoices):
    FEMININO = "F"
    MASCULINO = "M"


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=Sexo.choices)
    altura = models.FloatField()
    peso = models.FloatField()

    def __str__(self):
        return self.nome

    def __init__(self, id, pNome, pData, pCPF, pSexo, pAltura, pPeso, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if id is not None:
            self.id = id
        if pNome is not None:
            self.nome = pNome
        if pData is not None:
            self.data_nasc = pData
        if pCPF is not None:
            self.cpf = pCPF
        if pSexo is not None:
            self.sexo = pSexo
        if pAltura is not None:
            self.altura = pAltura
        if pPeso is not None:
            self.peso = pPeso

    def CalcularPesoIdeal(self):
        if self.sexo == "F":
            return (62.1 * self.altura) - 44.7
        else:
            return (72.7 * self.altura) - 58
