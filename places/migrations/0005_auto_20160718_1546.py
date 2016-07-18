# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20150329_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituency',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=(b'county__name',), editable=False),
        ),
        migrations.AlterField(
            model_name='county',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='district',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=(b'province__name',), editable=False),
        ),
        migrations.AlterField(
            model_name='division',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=(b'district__name',), editable=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=(b'division__name',), editable=False),
        ),
        migrations.AlterField(
            model_name='province',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='schoolzone',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=(b'county__name',), editable=False),
        ),
        migrations.AlterField(
            model_name='sublocation',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=(b'location__name',), editable=False),
        ),
    ]
