# Generated by Django 4.2.6 on 2023-12-06 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='type',
            new_name='news_type',
        ),
    ]
