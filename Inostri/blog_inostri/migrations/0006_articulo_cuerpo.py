# Generated by Django 4.2.1 on 2023-05-21 18:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_inostri', '0005_remove_articulo_cuerpo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
