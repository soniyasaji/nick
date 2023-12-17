# Generated by Django 4.2.6 on 2023-11-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hom_title', models.CharField(max_length=200)),
                ('hom_descrp', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='description',
            new_name='mag_descrp',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='image',
            new_name='mag_image',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='pdf',
            new_name='mag_pdf',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='price',
            new_name='mag_price',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='heading',
            new_name='mag_title',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='title',
        ),
    ]
