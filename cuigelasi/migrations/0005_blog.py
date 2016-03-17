# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuigelasi', '0004_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('blog_unique', models.CharField(max_length=30)),
                ('blog_unique1', models.CharField(max_length=30)),
                ('blog_TBtitle', models.CharField(max_length=60)),
                ('blog_title', models.CharField(max_length=60)),
                ('blog_content', models.CharField(max_length=9000)),
            ],
        ),
    ]
