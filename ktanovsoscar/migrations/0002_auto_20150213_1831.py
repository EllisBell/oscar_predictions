# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ktanovsoscar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='winner',
            field=models.ForeignKey(related_name=b'+', default=0, to='ktanovsoscar.Nominee'),
        ),
    ]
