import os, django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
from cardapio.models import Produto, Pedido


def criando_produtos(quantidade_de_produtos):
    fake = Faker("pt_BR")
    Faker.seed(10)
    for _ in range(quantidade_de_produtos):
        nome = fake.color_name()
        descricao = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis, fugiat dolorem asperiores voluptatem amet deserunt ullam cum quasi itaque quidem aut unde hic excepturi. Molestias, non distinctio! Dolore, laborum distinctio."
        preco = "{}.{}".format(random.randrange(10, 99), random.randrange(10, 99))
        tipo = random.choice("BC")
        data_cadastro = fake.date_between(start_date="-2y", end_date="today")
        produto = Produto(nome=nome, descricao=descricao, preco=preco, tipo=tipo, data_cadastro=data_cadastro)
        produto.save()


criando_produtos(20)
