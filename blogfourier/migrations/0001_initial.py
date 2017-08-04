# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 13:44
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
            name='blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('test', models.TextField(verbose_name='Texte')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Date de creation')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Date de Publication')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autheur')),
            ],
        ),
    ]