# Generated by Django 5.0.4 on 2024-05-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CZ', 'Cheese'), ('CR', 'Curd'), ('MS', 'Milkshake'), ('LS', 'Lassi'), ('ML', 'Milk'), ('IC', 'Ice-Creams'), ('PN', 'Paneer'), ('GH', 'Ghee')], max_length=2),
        ),
    ]
