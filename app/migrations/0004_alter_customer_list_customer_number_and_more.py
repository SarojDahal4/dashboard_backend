# Generated by Django 5.1.3 on 2024-11-15 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_customer_id_customer_list_customer_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_list',
            name='customer_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='product_list',
            name='product_number',
            field=models.IntegerField(unique=True),
        ),
    ]
