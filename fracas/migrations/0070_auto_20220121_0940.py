# Generated by Django 3.0.4 on 2022-01-21 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0069_auto_20220119_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failuredata',
            name='asset_config_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fracas.Asset', to_field='asset_config_id'),
        ),
    ]
