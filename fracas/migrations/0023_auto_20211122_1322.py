# Generated by Django 3.0.4 on 2021-11-22 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0022_auto_20211122_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defectdiscussion',
            name='attendees',
            field=models.ManyToManyField(blank=True, null=True, to='fracas.EmployeeMaster'),
        ),
    ]
