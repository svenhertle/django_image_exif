# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExifData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('focal_length', models.CharField(max_length=100, verbose_name='Focal length', blank=True)),
                ('iso', models.CharField(max_length=100, verbose_name='ISO', blank=True)),
                ('fraction', models.CharField(max_length=100, verbose_name='Fraction', blank=True)),
                ('exposure_time', models.CharField(max_length=100, verbose_name='Exposure time', blank=True)),
                ('image', models.OneToOneField(verbose_name='Image', to='filer.Image')),
            ],
            options={
                'verbose_name': 'EXIF Data',
                'verbose_name_plural': 'EXIF data',
            },
            bases=(models.Model,),
        ),
    ]
