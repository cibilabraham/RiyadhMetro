# Generated by Django 3.0.4 on 2021-12-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0042_temp_table_failuredata_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp_table_import_file',
            name='MART',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='temp_table_import_file',
            name='MTBF',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='temp_table_import_file',
            name='MTBR',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='temp_table_import_file',
            name='MTBSAF',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='temp_table_import_file',
            name='asset_quantity',
            field=models.TextField(),
        ),
    ]
