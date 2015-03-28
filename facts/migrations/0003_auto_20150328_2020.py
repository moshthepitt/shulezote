# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0002_auto_20150321_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fact',
            options={'ordering': ['name']},
        ),
    ]
