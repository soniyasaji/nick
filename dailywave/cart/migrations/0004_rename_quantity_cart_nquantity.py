# Generated by Django 4.2.6 on 2023-12-07 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_account_rename_news_type_cart_type_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='quantity',
            new_name='nquantity',
        ),
    ]
