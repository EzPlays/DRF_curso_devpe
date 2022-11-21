# Generated by Django 4.1.3 on 2022-11-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_historicalproduct_category_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='image',
            field=models.TextField(max_length=100, null=True, verbose_name='Imagen del Producto'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/', verbose_name='Imagen del Producto'),
        ),
    ]
