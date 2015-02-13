# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('number_noms', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votes', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='ktanovsoscar.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nominee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='nomination',
            name='nominee',
            field=models.ForeignKey(to='ktanovsoscar.Nominee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='noms',
            field=models.ManyToManyField(to='ktanovsoscar.Nominee', through='ktanovsoscar.Nomination'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='winner',
            field=models.ForeignKey(related_name=b'+', to='ktanovsoscar.Nominee'),
            preserve_default=True,
        ),
    ]
