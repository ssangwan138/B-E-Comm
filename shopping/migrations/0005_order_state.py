# Generated by Django 4.0.4 on 2022-05-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0004_rename_orders_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]
