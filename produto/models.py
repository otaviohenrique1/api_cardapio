from django.db import models


class Produto(models.Model):
    TIPO = (
        ("", "Selecione"),
        ("B", "Bebida"),
        ("C", "Comida"),
    )

    nome = models.CharField(max_length=200, blank=False)
    descricao = models.TextField(blank=False)
    preco = models.DecimalField(max_length=20, blank=False)
    tipo = models.CharField(
        max_length=1, choices=TIPO, blank=False, null=False, default=""
    )
    data_cadastro = models.DateTimeField()
    foto = models.ImageField(blank=True)

    def __str__(self):
        return "{} - R$ {}".format(self.nome, self.preco)
