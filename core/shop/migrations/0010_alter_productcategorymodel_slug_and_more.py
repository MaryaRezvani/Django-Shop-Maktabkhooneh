# Generated by Django 4.2.10 on 2024-03-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_productimagemodel_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategorymodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]