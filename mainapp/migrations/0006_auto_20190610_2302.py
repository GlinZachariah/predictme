# Generated by Django 2.1.7 on 2019-06-10 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190610_2249'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrainData_MSFT',
            new_name='PredictData_CSCO',
        ),
        migrations.RenameModel(
            old_name='TrainData_CSCO',
            new_name='PredictData_MSFT',
        ),
        migrations.RenameField(
            model_name='predictdata_csco',
            old_name='weighted_adj_close',
            new_name='weighted_adj_close_price',
        ),
        migrations.RenameField(
            model_name='predictdata_csco',
            old_name='weighted_close',
            new_name='weighted_close_price',
        ),
        migrations.RenameField(
            model_name='predictdata_msft',
            old_name='weighted_adj_close',
            new_name='weighted_adj_close_price',
        ),
        migrations.RenameField(
            model_name='predictdata_msft',
            old_name='weighted_close',
            new_name='weighted_close_price',
        ),
    ]
