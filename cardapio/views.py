from django.shortcuts import render
from cardapio.models import Produto, Pedido
from rest_framework import viewsets
from cardapio.serializer import ProdutoSerializer, PedidoSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""

    queryset = Produto.objects.all()

    def get_serializer_class(self):
        return ProdutoSerializer


class PedidosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os pedidos"""

    queryset = Pedido.objects.all()

    def get_serializer_class(self):
        return PedidoSerializer
