# Generated by Django 4.0.4 on 2022-07-31 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0002_proposta_ehnegada'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='temProposta',
            field=models.BooleanField(default=False),
        ),
    ]
