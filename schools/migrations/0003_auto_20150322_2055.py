# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_auto_20150321_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(default=b'Z', help_text='Day, Boarding or Both?', max_length=1, verbose_name='School Type', choices=[(b'1', 'Day'), (b'2', 'Boarding'), (b'3', 'Day & Boarding'), (b'Z', 'N/A')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='sponsor',
            field=models.CharField(default=b'Z', max_length=1, verbose_name='School Sponsor', choices=[(b'1', 'Central Government/DEB'), (b'2', 'Religious Organisation'), (b'3', 'Community'), (b'4', 'NGO/CBO'), (b'5', 'Private Individual'), (b'Z', 'N/A')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='student_gender',
            field=models.CharField(default=b'Z', help_text='Boys school, Girls school, or mixed', max_length=1, verbose_name='Student Gender', choices=[(b'1', 'Boys'), (b'2', 'Girls'), (b'3', 'Mixed'), (b'Z', 'N/A')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='school',
            name='student_needs',
            field=models.CharField(default=b'1', help_text='Ordinary, Special or Integrated', max_length=1, verbose_name='Student Needs', choices=[(b'1', 'Ordinary'), (b'2', 'Special'), (b'3', 'Integrated')]),
            preserve_default=True,
        ),
    ]
