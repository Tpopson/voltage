# Generated by Django 4.0.5 on 2022-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_max_product_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='max',
            field=models.IntegerField(),
        ),
    ]
