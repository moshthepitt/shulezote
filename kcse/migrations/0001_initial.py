# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20150328_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('district_code', models.CharField(max_length=255, verbose_name='District Code', blank=True)),
                ('school_code', models.CharField(max_length=255, verbose_name='School Code', blank=True)),
                ('knec_code', models.CharField(max_length=255, verbose_name='KNEC Code', blank=True)),
                ('gender', models.CharField(help_text='Gender', max_length=1, verbose_name='Gender', choices=[(b'1', 'Male'), (b'2', 'Female')])),
                ('grade', models.CharField(max_length=2, verbose_name='Grade')),
                ('mean_grade', models.DecimalField(verbose_name='Mean Grade', max_digits=5, decimal_places=2)),
                ('frequency', models.IntegerField(verbose_name='Frequency')),
                ('school', models.ForeignKey(verbose_name='School', to='schools.School')),
            ],
            options={
                'verbose_name': 'KCSE Result',
                'verbose_name_plural': 'KCSE Results',
            },
            bases=(models.Model,),
        ),
    ]
