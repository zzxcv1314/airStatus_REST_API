# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-19 05:00
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='airstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm25', models.CharField(max_length=30)),
                ('pm10', models.CharField(max_length=30)),
                ('temperature', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('dname', models.CharField(max_length=30)),
                ('dlocation', models.CharField(max_length=30)),
                ('dkey', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False)),
                ('downer', models.CharField(editable=False, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
