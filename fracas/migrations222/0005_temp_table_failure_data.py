# Generated by Django 3.0.4 on 2021-12-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0004_delete_temp_table_failure_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp_table_failure_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failure_id', models.IntegerField(null=True)),
                ('asset_type', models.TextField()),
                ('asset_config_id', models.TextField()),
                ('asset_type_id', models.TextField()),
                ('event_description', models.TextField()),
                ('mode_id', models.TextField()),
                ('date', models.TextField()),
                ('time', models.TextField()),
                ('detection', models.TextField()),
                ('service_delay', models.TextField()),
                ('immediate_investigation', models.TextField()),
                ('failure_type', models.TextField()),
                ('safety_failure', models.TextField()),
                ('hazard_id', models.TextField()),
                ('cm_description', models.TextField()),
                ('replaced_asset_config_id', models.TextField()),
                ('cm_start_date', models.TextField()),
                ('cm_start_time', models.TextField()),
                ('cm_end_date', models.TextField()),
                ('cm_end_time', models.TextField()),
                ('oem_failure_reference', models.TextField()),
                ('defect', models.TextField()),
                ('error_list', models.TextField()),
                ('P_id', models.TextField()),
                ('updated_by', models.TextField()),
            ],
        ),
    ]
