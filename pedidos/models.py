from django.db import models

class Pedidos(models.Model):
    cliente = models.CharField(max_length=200, blank=False)
    endereco = models.CharField(max_length=200, blank=False)
    descricao = models.TextField(blank=False)
    lista_produtos = models.JSONField(blank=False)
    preco_total = models.DecimalField(max_length=20, blank=False)
    
    
    
