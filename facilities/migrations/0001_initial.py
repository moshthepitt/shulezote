# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255, verbose_name='Name of facility')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FacilityRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('period', models.DateField(verbose_name='Period')),
                ('boys', models.PositiveIntegerField(default=0, verbose_name='Boys')),
                ('girls', models.PositiveIntegerField(default=0, verbose_name='Girls')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Total')),
                ('facility', models.ForeignKey(verbose_name='Facility', to='facilities.Facility')),
                ('school', models.ForeignKey(verbose_name='School', to='schools.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
