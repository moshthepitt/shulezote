# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20150322_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constituency',
            options={'verbose_name': 'Constituency', 'verbose_name_plural': 'Constituencies'},
        ),
        migrations.AlterModelOptions(
            name='county',
            options={'verbose_name': 'County', 'verbose_name_plural': 'Counties'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name': 'District', 'verbose_name_plural': 'Districts'},
        ),
        migrations.AlterModelOptions(
            name='division',
            options={'verbose_name': 'Division', 'verbose_name_plural': 'Divisions'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Location', 'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': 'Province', 'verbose_name_plural': 'Provinces'},
        ),
        migrations.AlterModelOptions(
            name='schoolzone',
            options={'verbose_name': 'School Zone', 'verbose_name_plural': 'School Zones'},
        ),
        migrations.AlterModelOptions(
            name='sublocation',
            options={'verbose_name': 'Sub Location', 'verbose_name_plural': 'Sub Locations'},
        ),
    ]
