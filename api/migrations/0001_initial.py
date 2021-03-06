# Generated by Django 4.0.4 on 2022-04-21 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='title')),
                ('text', models.TextField(blank=True, max_length=1000, verbose_name='text')),
                ('photo', models.CharField(blank=True, max_length=200, null=True, verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(blank=True, max_length=200, null=True, verbose_name='image')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=600, null=True, verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, verbose_name='tag_name')),
            ],
        ),
        migrations.CreateModel(
            name='Consulting_Center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.CharField(blank=True, max_length=200, null=True, verbose_name='image')),
                ('address', models.CharField(max_length=200, verbose_name='address')),
                ('is_online', models.BooleanField(default=False, verbose_name='online_status')),
                ('phone', models.CharField(blank=True, max_length=50, unique=True, verbose_name='phone')),
                ('email', models.CharField(max_length=250, unique=True, verbose_name='email')),
                ('tags', models.ManyToManyField(to='api.tag')),
            ],
        ),
    ]
