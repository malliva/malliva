# Generated by Django 3.2 on 2021-06-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentGateway',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('handler_name', models.CharField(help_text='Name of the payment gateway', max_length=200)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
