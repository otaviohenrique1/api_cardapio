from django.contrib import admin
from cardapio.models import Produto, Pedido


class Produtos(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "preco", "tipo", "data_cadastro", "foto")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)

admin.site.register(Produto, Produtos)

class Pedidos(admin.ModelAdmin):
    list_display = ("id", "cliente", "endereco", "descricao", "lista_produtos", "preco_total")
    list_display_links = ("id", "cliente")
    search_fields = ("cliente",)

admin.site.register(Pedido, Pedidos)
