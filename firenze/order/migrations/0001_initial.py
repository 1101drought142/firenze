# Generated by Django 5.1.2 on 2024-11-16 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата заказа')),
                ('order_type', models.CharField(choices=[('Доставка', 'Delivery'), ('Забрать из магазина', 'Pick Up')], max_length=127, verbose_name='Тип заказа')),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personal.customer')),
            ],
        ),
    ]