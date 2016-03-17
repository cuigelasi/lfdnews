# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('blog_unique', models.CharField(max_length=30)),
                ('blog_title', models.CharField(max_length=60)),
                ('blog_content', models.CharField(max_length=100)),
            ],
        ),
    ]
