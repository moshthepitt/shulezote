# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20150328_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constituency',
            options={'ordering': ['name'], 'verbose_name': 'Constituency', 'verbose_name_plural': 'Constituencies'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'ordering': ['name'], 'verbose_name': 'County', 'verbose_name_plural': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['name'], 'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['name'], 'verbose_name': 'Division', 'verbose_name_plural': 'Divisions'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['name'], 'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'ordering': ['name'], 'verbose_name': 'Province', 'verbose_name_plural': 'Provinces'},
        ),
        migrations.AlterModelOptions(
            name='schoolzone',
            options={'ordering': ['name'], 'verbose_name': 'School Zone', 'verbose_name_plural': 'School Zones'},
        ),
        migrations.AlterModelOptions(
            name='sublocation',
            options={'ordering': ['name'], 'verbose_name': 'Sub Location', 'verbose_name_plural': 'Sub Locations'},
        ),
    ]
