# Generated by Django 3.0.4 on 2021-11-12 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0006_auto_20211111_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbsmaster',
            name='is_active',
            field=models.IntegerField(default=0),
        ),
    ]
