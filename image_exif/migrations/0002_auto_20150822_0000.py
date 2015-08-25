# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_image_exif', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exifdata',
            options={'verbose_name': 'EXIF Data', 'verbose_name_plural': 'EXIF data'},
        ),
        migrations.AlterField(
            model_name='exifdata',
            name='exposure_time',
            field=models.CharField(max_length=100, verbose_name='Exposure time', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exifdata',
            name='focal_length',
            field=models.CharField(max_length=100, verbose_name='Focal length', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exifdata',
            name='fraction',
            field=models.CharField(max_length=100, verbose_name='Fraction', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='exifdata',
            name='iso',
            field=models.CharField(max_length=100, verbose_name='ISO', blank=True),
            preserve_default=True,
        ),
    ]
