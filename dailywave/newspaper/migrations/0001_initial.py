# Generated by Django 4.2.6 on 2023-10-31 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('heading', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('pdf', models.FileField(upload_to='news/pdf')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/cover')),
            ],
        ),
    ]
