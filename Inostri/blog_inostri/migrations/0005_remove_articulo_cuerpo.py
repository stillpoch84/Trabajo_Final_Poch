# Generated by Django 4.2.1 on 2023-05-21 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_inostri', '0004_alter_articulo_cuerpo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='cuerpo',
        ),
    ]
