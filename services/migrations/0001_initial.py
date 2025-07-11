# Generated by Django 5.2.3 on 2025-06-23 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('base_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('state', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'service_type',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('custom_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateField()),
                ('payment_status', models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Paid'), (2, 'Partially Paid')])),
                ('state', models.SmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='clients.client')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='services.servicetype')),
            ],
            options={
                'db_table': 'service',
            },
        ),
    ]
