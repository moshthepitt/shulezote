# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('code', models.CharField(max_length=255, verbose_name='Code', blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name of School')),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('address', models.CharField(max_length=255, verbose_name='Address', blank=True)),
                ('level', models.CharField(help_text='Primary or secondary school', max_length=1, verbose_name='Level', choices=[(b'1', 'Primary School'), (b'2', 'Secondary School')])),
                ('school_type', models.CharField(default=b'1', help_text='Day, Boarding or Both?', max_length=1, verbose_name='School Type', choices=[(b'1', 'Day'), (b'2', 'Boarding'), (b'3', 'Day & Boarding')])),
                ('student_gender', models.CharField(default=b'3', help_text='Boys school, Girls school, or mixed', max_length=1, verbose_name='Student Gender', choices=[(b'1', 'Boys'), (b'2', 'Girls'), (b'3', 'Mixed')])),
                ('ownership', models.CharField(default=b'1', help_text='Private or public', max_length=1, verbose_name='Ownership', choices=[(b'1', 'Public'), (b'2', 'Private')])),
                ('sponsor', models.CharField(default=b'1', max_length=1, verbose_name='School Sponsor', choices=[(b'1', 'Central Government/DEB'), (b'2', 'Religious Organisation'), (b'3', 'Community'), (b'4', 'NGO/CBO'), (b'5', 'Private Individual')])),
                ('student_needs', models.CharField(default=b'1', help_text='Ordinary, Special or Integrated', max_length=1, verbose_name='Student Needs', choices=[(b'1', 'Ordnirary'), (b'2', 'Special'), (b'3', 'Integrated')])),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this school is active.', verbose_name='Active')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(help_text='Represented as (longitude, latitude)', srid=4326, verbose_name='Coordinates')),
                ('constituency', models.ForeignKey(verbose_name='Constituency', to='places.Constituency')),
                ('county', models.ForeignKey(verbose_name='County', to='places.County')),
                ('district', models.ForeignKey(default=None, blank=True, to='places.District', null=True, verbose_name='District')),
                ('division', models.ForeignKey(default=None, blank=True, to='places.Division', null=True, verbose_name='Division')),
                ('location', models.ForeignKey(default=None, blank=True, to='places.Location', null=True, verbose_name='Location')),
                ('province', models.ForeignKey(default=None, blank=True, to='places.Province', null=True, verbose_name='Province')),
                ('school_sone', models.ForeignKey(default=None, blank=True, to='places.SchoolZone', null=True, verbose_name='School Zone')),
                ('sub_location', models.ForeignKey(default=None, blank=True, to='places.SubLocation', null=True, verbose_name='Sub Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
