# Generated by Django 4.2.6 on 2023-10-31 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_alter_newspaper_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='heading',
            field=models.CharField(max_length=200),
        ),
    ]