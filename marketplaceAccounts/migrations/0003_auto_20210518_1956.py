# Generated by Django 3.0.5 on 2021-05-18 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaceAccounts', '0002_auto_20210517_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplaceaccount',
            name='marketplace_id',
            field=models.UUIDField(default='40b67c27a1a34adbbbe2566f4ca90be1', primary_key=True, serialize=False),
        ),
    ]