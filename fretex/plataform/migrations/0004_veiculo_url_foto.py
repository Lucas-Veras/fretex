# Generated by Django 4.0.4 on 2022-08-14 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataform', '0003_alter_cliente_url_foto_alter_freteiro_url_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='url_foto',
            field=models.ImageField(blank=True, null=True, upload_to='veiculo'),
        ),
    ]
