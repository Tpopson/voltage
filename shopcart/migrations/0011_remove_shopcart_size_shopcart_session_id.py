# Generated by Django 4.0.5 on 2022-07-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0010_remove_shopcart_subtotal_alter_shopcart_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopcart',
            name='size',
        ),
        migrations.AddField(
            model_name='shopcart',
            name='session_id',
            field=models.CharField(default='a', max_length=100),
        ),
    ]