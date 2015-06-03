# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('status', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='productoption',
            options={'managed': False, 'verbose_name': 'Plan', 'verbose_name_plural': 'Plans'},
        ),
    ]
