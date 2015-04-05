# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kcse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='school',
            field=models.ForeignKey(related_name='kcse_result', verbose_name='School', to='schools.School'),
            preserve_default=True,
        ),
    ]
