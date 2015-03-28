# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['-is_teacher', 'staff_type']},
        ),
        migrations.AlterField(
            model_name='staff',
            name='is_teacher',
            field=models.BooleanField(default=True, help_text='Is this staff member is a teacher', verbose_name='Teacher'),
            preserve_default=True,
        ),
    ]
