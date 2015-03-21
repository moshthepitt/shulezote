# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='school_sone',
            new_name='school_zone',
        ),
    ]
