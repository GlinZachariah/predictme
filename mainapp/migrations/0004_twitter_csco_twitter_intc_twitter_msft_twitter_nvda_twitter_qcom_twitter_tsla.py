# Generated by Django 2.1.7 on 2019-04-16 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_csco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter_CSCO',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.TextField()),
                ('tweet_date', models.DateField(verbose_name='date')),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_INTC',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.TextField()),
                ('tweet_date', models.DateField(verbose_name='date')),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_MSFT',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.TextField()),
                ('tweet_date', models.DateField(verbose_name='date')),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_NVDA',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.TextField()),
                ('tweet_date', models.DateField(verbose_name='date')),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_QCOM',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.TextField()),
                ('tweet_date', models.DateField(verbose_name='date')),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter_TSLA',
            fields=[
                ('tweet_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tweet_text', models.TextField()),
                ('tweet_date', models.DateField(verbose_name='date')),
                ('follower_count', models.IntegerField(default=0)),
            ],
        ),
    ]
