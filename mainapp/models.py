from django.db import models

# Create your models here.

class MSFT(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

class CSCO(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)


class Twitter_MSFT(models.Model):
    tweet_id= models.BigIntegerField(primary_key=True)
    tweet_text = models.TextField()
    tweet_date = models.DateField('date')
    follower_count = models.IntegerField(default=0)

class Twitter_CSCO(models.Model):
    tweet_id= models.BigIntegerField(primary_key=True)
    tweet_text = models.TextField()
    tweet_date = models.DateField('date')
    follower_count = models.IntegerField(default=0)

class PredictData_MSFT(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    sentiment = models.FloatField(default=0.0)
    weighted_close_price = models.FloatField(default=0.0)
    weighted_adj_close_price = models.FloatField(default=0.0)

class PredictData_CSCO(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)
    sentiment = models.FloatField(default=0.0)
    weighted_close_price = models.FloatField(default=0.0)
    weighted_adj_close_price = models.FloatField(default=0.0)