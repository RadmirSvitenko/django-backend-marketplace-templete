# Generated by Django 5.1.4 on 2025-01-07 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_slug_alter_productclass_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_class',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.productclass', verbose_name='Класс продукта'),
        ),
    ]
