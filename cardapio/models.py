from django.db import models


class Produto(models.Model):
    TIPO = (
        ("", "Selecione"),
        ("B", "Bebida"),
        ("C", "Comida"),
    )

    nome = models.CharField(max_length=200, blank=False)
    descricao = models.TextField(blank=False)
    preco = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    tipo = models.CharField(
        max_length=1, choices=TIPO, blank=False, null=False, default=""
    )
    data_cadastro = models.DateTimeField()
    foto = models.ImageField(blank=True)
    # pedido = models.ManyToOneRel().many_to_one(True)

    def __str__(self):
        return "{} - R$ {}".format(self.nome, self.preco)


class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=200, blank=False)
    cliente = models.CharField(max_length=200, blank=False)
    endereco = models.CharField(max_length=200, blank=False)
    descricao = models.TextField(blank=False)
    preco_total = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    lista_produtos = models.TextField(blank=False)
    produtos = models.ForeignKey(
        to=Produto,
        related_name="produtos",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
