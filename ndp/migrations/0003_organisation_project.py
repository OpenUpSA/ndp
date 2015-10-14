# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ndp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ndp', '0002_auto_20151013_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('tel', models.CharField(max_length=100, blank=True)),
                ('email', models.EmailField(help_text=b'Contact email address', max_length=254, blank=True)),
                ('website', models.URLField(help_text=b'Website', blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('logo', models.ImageField(null=True, upload_to=ndp.models.image_filename, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(help_text=b'Website', blank=True)),
                ('description', models.TextField(default=b'', blank=True)),
                ('email', models.EmailField(help_text=b'Contact email address', max_length=254, blank=True)),
                ('organisation', models.ForeignKey(related_name='projects', to='ndp.Organisation')),
                ('sectors', models.ManyToManyField(related_name='projects', to='ndp.Sector')),
            ],
        ),
    ]
