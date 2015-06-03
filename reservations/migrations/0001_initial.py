# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('reserved', models.IntegerField()),
                ('available', models.IntegerField()),
                ('purchased', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'products_options',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_id', models.IntegerField()),
                ('product_option_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('company', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('terms', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('amount', models.DecimalField(max_digits=8, decimal_places=2)),
                ('transaction_id', models.CharField(max_length=255)),
                ('payer_id', models.CharField(max_length=255)),
                ('completed_at', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'reservations',
                'managed': False,
            },
        ),
    ]
