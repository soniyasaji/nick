# Generated by Django 4.2.6 on 2023-12-07 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0009_rename_newspaper_news_type_newsc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news_type',
            old_name='nstock',
            new_name='stock',
        ),
    ]