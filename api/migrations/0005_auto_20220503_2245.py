# Generated by Django 3.2.9 on 2022-05-03 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_consulting_center_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulting_center',
            name='website',
            field=models.CharField(blank=True, max_length=500, verbose_name='website'),
        ),
        migrations.AlterField(
            model_name='consulting_center',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='consulting_center',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='consulting_center',
            name='phone',
            field=models.CharField(blank=True, max_length=50, verbose_name='phone'),
        ),
    ]
