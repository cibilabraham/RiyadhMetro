# Generated by Django 3.1.6 on 2022-01-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0065_auto_20220113_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failuredata',
            name='cm_end_date',
            field=models.DateField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='failuredata',
            name='cm_end_time',
            field=models.TimeField(blank=True, max_length=15, null=True),
        ),
    ]
