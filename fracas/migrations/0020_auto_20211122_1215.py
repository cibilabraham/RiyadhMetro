# Generated by Django 3.0.4 on 2021-11-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0019_auto_20211122_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defectdiscussion',
            name='attendees',
            field=models.ManyToManyField(blank=True, to='fracas.EmployeeMaster'),
        ),
    ]
