# Generated by Django 4.0.5 on 2022-06-08 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_featured_product_latest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=50)),
                ('carousel', models.ImageField(default='slide.jpg', upload_to='carousel')),
            ],
        ),
    ]
