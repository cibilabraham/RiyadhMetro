# Generated by Django 3.1.6 on 2022-01-10 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0054_auto_20220105_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbsmaster',
            name='product_description',
            field=models.CharField(blank=True, max_length=550),
        ),
        migrations.AlterField(
            model_name='pbsmaster',
            name='product_id',
            field=models.CharField(blank=True, max_length=550),
        ),
        migrations.AlterField(
            model_name='pbsmaster',
            name='subsystem',
            field=models.CharField(blank=True, max_length=550),
        ),
        migrations.AlterField(
            model_name='pbsmaster',
            name='system',
            field=models.CharField(blank=True, max_length=550),
        ),
    ]
