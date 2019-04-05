from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import TSLA
import sqlite3
import pandas as pd 
from modules.make_graph import graph,find_price


def index(request):
    template = loader.get_template('index.html')
    context = {
        'test_message' : 'working',
    }
    return HttpResponse(template.render(context, request))

def base(request,symbol):
    template = loader.get_template('base.html')
    cnx = sqlite3.connect('db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM mainapp_"+symbol.lower(), cnx)
    df.price_date =pd.to_datetime(df.price_date)
    df = df.sort_values('price_date')
    #DISPLAY GRAPH
    # graph(symbol,df)
    secondlast_price,last_price =find_price(symbol,df)
    dt = df['price_date'].values;
    close_date = pd.Timestamp(dt[len(dt)-1]).date()
    change = secondlast_price -last_price
    per  = (change/last_price)*100
    change ='%.2f'%(change)
    per ='%.2f'%(per)
    if change[0] != '-' :
        change="+"+change
    last_price ='%.2f'%(last_price)
    context = {
        'symbol' : symbol,
        'temp':df,
        'change': change,
        'last_price': last_price,
        'per':per,
        'close_date':close_date,
    }
    return HttpResponse(template.render(context, request))