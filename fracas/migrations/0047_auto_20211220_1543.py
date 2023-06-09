# Generated by Django 3.1.6 on 2021-12-20 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fracas', '0046_history_temp_table_failure_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pbsmaster',
            old_name='MTBR',
            new_name='MTTR',
        ),
        migrations.AddField(
            model_name='pbsmaster',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fracas.product'),
        ),
        migrations.AlterField(
            model_name='pbsmaster',
            name='subsystem',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
