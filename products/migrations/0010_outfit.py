# Generated by Django 3.2.23 on 2024-04-04 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_delete_outfit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('full_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('product_list', models.ManyToManyField(related_name='product_list', to='products.Product')),
            ],
            bases=('products.product',),
        ),
    ]
