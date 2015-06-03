# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20150603_0924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'managed': False},
        ),
    ]
