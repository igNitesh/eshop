# Generated by Django 2.2.12 on 2022-04-30 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prce',
            new_name='price',
        ),
    ]
