# Generated by Django 3.0.4 on 2021-11-19 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0015_delete_tempfailuredata'),
    ]

    operations = [
        migrations.AddField(
            model_name='rootcause',
            name='P_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rootcause',
            name='is_active',
            field=models.IntegerField(default=0),
        ),
    ]
