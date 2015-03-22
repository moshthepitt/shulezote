# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constituency',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='schoolzone',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='sublocation',
            options={'ordering': ['name']},
        ),
    ]
