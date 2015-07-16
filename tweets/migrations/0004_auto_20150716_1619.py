# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_auto_20150714_0143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='tag',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tag',
            field=models.ManyToManyField(to='tweets.Tag'),
        ),
    ]
