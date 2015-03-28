# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20150322_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school',
            options={'ordering': ['name'], 'verbose_name': 'School', 'verbose_name_plural': 'Schools'},
        ),
    ]
