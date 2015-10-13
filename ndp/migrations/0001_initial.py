# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Full name of the sector', unique=True, max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('vision', models.TextField(default=b'', help_text=b'Full vision (HTML allowed)', blank=True)),
                ('goals', models.TextField(default=b'', help_text=b'List of goals, one per line.', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
