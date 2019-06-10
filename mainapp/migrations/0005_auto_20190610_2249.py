# Generated by Django 2.1.7 on 2019-06-10 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_twitter_csco_twitter_intc_twitter_msft_twitter_nvda_twitter_qcom_twitter_tsla'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainData_CSCO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_date', models.DateField(verbose_name='date')),
                ('open_price', models.FloatField(default=0.0)),
                ('high_price', models.FloatField(default=0.0)),
                ('low_price', models.FloatField(default=0.0)),
                ('close_price', models.FloatField(default=0.0)),
                ('adj_close_price', models.FloatField(default=0.0)),
                ('volume', models.FloatField(default=0.0)),
                ('sentiment', models.FloatField(default=0.0)),
                ('weighted_close', models.FloatField(default=0.0)),
                ('weighted_adj_close', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='TrainData_MSFT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_date', models.DateField(verbose_name='date')),
                ('open_price', models.FloatField(default=0.0)),
                ('high_price', models.FloatField(default=0.0)),
                ('low_price', models.FloatField(default=0.0)),
                ('close_price', models.FloatField(default=0.0)),
                ('adj_close_price', models.FloatField(default=0.0)),
                ('volume', models.FloatField(default=0.0)),
                ('sentiment', models.FloatField(default=0.0)),
                ('weighted_close', models.FloatField(default=0.0)),
                ('weighted_adj_close', models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name='INTC',
        ),
        migrations.DeleteModel(
            name='IXIC',
        ),
        migrations.DeleteModel(
            name='NVDA',
        ),
        migrations.DeleteModel(
            name='QCOM',
        ),
        migrations.DeleteModel(
            name='TSLA',
        ),
        migrations.DeleteModel(
            name='Twitter_INTC',
        ),
        migrations.DeleteModel(
            name='Twitter_NVDA',
        ),
        migrations.DeleteModel(
            name='Twitter_QCOM',
        ),
        migrations.DeleteModel(
            name='Twitter_TSLA',
        ),
    ]
