# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('currencies', django_mysql.models.JSONField(default=dict)),
            ],
        ),
    ]
