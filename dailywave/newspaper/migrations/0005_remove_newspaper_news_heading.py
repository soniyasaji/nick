# Generated by Django 4.2.6 on 2023-12-01 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0004_rename_description_newspaper_news_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspaper',
            name='news_heading',
        ),
    ]
