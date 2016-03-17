# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuigelasi', '0005_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoBlogMap',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('PhotoBlogMap_blogtitle', models.CharField(max_length=30)),
                ('PhotoBlogMap_phototype', models.CharField(max_length=30)),
                ('PhotoBlogMap_phototitle', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='blog_TBtitle',
            new_name='photo_name',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_unique',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='blog_unique1',
        ),
    ]
