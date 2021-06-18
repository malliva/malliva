# Generated by Django 3.0.5 on 2021-06-18 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('settingsManager', '0002_auto_20210528_1612'),
        ('marketplaceAccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('plan_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='marketplaceaccount',
            old_name='marketplace_admin',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='marketplaceaccount',
            old_name='usedomain',
            new_name='use_domain',
        ),
        migrations.RemoveField(
            model_name='marketplaceaccount',
            name='marketplace_plan_id',
        ),
        migrations.AddField(
            model_name='marketplaceaccount',
            name='configuration',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='settingsManager.Configuration'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('last_subscription_date', models.DateTimeField()),
                ('expiration_date', models.DateTimeField()),
                ('current_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplaceAccounts.Plan')),
            ],
        ),
        migrations.AddField(
            model_name='marketplaceaccount',
            name='marketplace_plan',
            field=models.ForeignKey(default='trial', on_delete=django.db.models.deletion.SET_DEFAULT, to='marketplaceAccounts.Plan'),
        ),
        migrations.AddField(
            model_name='marketplaceaccount',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='marketplaceAccounts.Subscription'),
        ),
    ]