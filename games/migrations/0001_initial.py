# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to=b'games/games_img')),
                ('description', models.TextField(blank=True, null=True)),
                ('release_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('developers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.Developer')),
            ],
            options={
                'ordering': ('-release_date',),
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('genre',),
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='games.Genre'),
        ),
        migrations.AlterIndexTogether(
            name='game',
            index_together=set([('id', 'slug')]),
        ),
    ]
