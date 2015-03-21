# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('period', models.DateField(verbose_name='Period')),
                ('staff_type', models.CharField(max_length=1, verbose_name='Type of staff', choices=[(b'A', 'TSC Male Teachers'), (b'B', 'TSC Female Teachers'), (b'C', 'Local Authority Male Teachers'), (b'D', 'Local Authority Female Teachers'), (b'E', 'PTA Board of Governors Male Teacher'), (b'F', 'PTA Board of Governors Female Teacher'), (b'G', 'Other Male Teachers'), (b'H', 'Other Female Teachers'), (b'I', 'Non Teaching Staff Male'), (b'J', 'Non Teaching Staff Female')])),
                ('number', models.PositiveIntegerField(default=0, verbose_name='Number')),
                ('is_teacher', models.BooleanField(default=True, help_text='Designates whether this staff member is a teacher', verbose_name='Teacher')),
                ('school', models.ForeignKey(verbose_name='School', to='schools.School')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
