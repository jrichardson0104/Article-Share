# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_auto_20150716_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
    ]
