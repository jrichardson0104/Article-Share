# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20150714_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='posted',
            field=models.DateField(auto_now_add=True),
        ),
    ]
