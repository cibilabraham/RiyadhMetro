# Generated by Django 3.0.4 on 2021-12-17 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0005_temp_table_failure_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='temp_table_failure_data',
        ),
    ]
