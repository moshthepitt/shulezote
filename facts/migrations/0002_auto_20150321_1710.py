# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('facilities', '0001_initial'),
        ('schools', '0001_initial'),
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255, verbose_name='Fact')),
                ('value', models.CharField(max_length=255, verbose_name='Fact Value')),
                ('period', models.DateField(verbose_name='Period')),
                ('facility', models.ForeignKey(default=None, blank=True, to='facilities.Facility', null=True, verbose_name='Facility')),
                ('school', models.ForeignKey(verbose_name='School', to='schools.School')),
                ('staff', models.ForeignKey(default=None, blank=True, to='staff.Staff', null=True, verbose_name='Staff')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='facts',
            name='facility',
        ),
        migrations.RemoveField(
            model_name='facts',
            name='school',
        ),
        migrations.RemoveField(
            model_name='facts',
            name='staff',
        ),
        migrations.DeleteModel(
            name='Facts',
        ),
    ]
