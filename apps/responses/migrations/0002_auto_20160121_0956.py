# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('responses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='verbresponse',
            name='profile',
        ),
        migrations.AddField(
            model_name='verbresponse',
            name='session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='verbs', to='responses.ResponseSession'),
            preserve_default=False,
        ),
    ]
