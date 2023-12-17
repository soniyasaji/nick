# Generated by Django 4.2.6 on 2023-11-29 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0003_alter_newspaper_heading'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspaper',
            old_name='description',
            new_name='news_desc',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='heading',
            new_name='news_heading',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='image',
            new_name='news_image',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='pdf',
            new_name='news_pdf',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='price',
            new_name='news_price',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='title',
            new_name='news_title',
        ),
    ]
