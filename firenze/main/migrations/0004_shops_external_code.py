# Generated by Django 5.1.2 on 2025-01-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_shops_shop_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='shops',
            name='external_code',
            field=models.CharField(default='', max_length=127, verbose_name='Внешний код'),
        ),
    ]
