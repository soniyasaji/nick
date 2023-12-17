# Generated by Django 4.2.6 on 2023-12-06 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newspaper', '0009_rename_newspaper_news_type_newsc'),
        ('cart', '0002_rename_type_cart_news_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctnumber', models.IntegerField()),
                ('accttype', models.CharField(max_length=200)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='cart',
            old_name='news_type',
            new_name='type',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noofitems', models.IntegerField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=200)),
                ('order_status', models.CharField(default='pending', max_length=20)),
                ('delivery_status', models.CharField(default='pending', max_length=30)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaper.news_type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]