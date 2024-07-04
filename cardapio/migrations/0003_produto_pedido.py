# Generated by Django 5.0.6 on 2024-07-03 23:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_alter_pedido_lista_produtos'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='cardapio.pedido'),
        ),
    ]
