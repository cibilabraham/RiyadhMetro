# Generated by Django 3.0.4 on 2022-01-25 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0070_auto_20220121_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='function_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
