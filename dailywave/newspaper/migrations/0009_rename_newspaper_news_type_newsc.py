# Generated by Django 4.2.6 on 2023-12-03 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0008_rename_available_news_type_navailable_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news_type',
            old_name='newspaper',
            new_name='newsc',
        ),
    ]