# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-06 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRepresentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('representative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representatives', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='represented_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User representative',
                'verbose_name_plural': 'User representatives',
            },
        ),
    ]
