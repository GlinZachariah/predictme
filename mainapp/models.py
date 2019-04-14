from django.db import models

# Create your models here.
class TSLA(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

class INTC(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

class NVDA(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

class QCOM(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

class MSFT(models.Model):
    price_date= models.DateField('date')
    open_price = models.FloatField(default=0.0)
    high_price = models.FloatField(default=0.0)
    low_price = models.FloatField(default=0.0)
    close_price = models.FloatField(default=0.0)
    adj_close_price = models.FloatField(default=0.0)
    volume = models.FloatField(default=0.0)

class IXIC(models.Model):
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

# class NEWS(models.Model):
#     news_date =models.DateTimeField('news date')
#     news_ticker =models.DateTimeField('news date')