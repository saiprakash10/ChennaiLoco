# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-11 05:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('locality', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
                ('line', models.CharField(max_length=10)),
                ('majorStation', models.BooleanField(default=0)),
                ('slug', models.SlugField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('stations', models.ManyToManyField(related_name='stations', through='train.Route', to='train.Station')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.Train'),
        ),
    ]