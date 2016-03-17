# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuigelasi', '0003_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
