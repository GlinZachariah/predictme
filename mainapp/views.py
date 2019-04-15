from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import sqlite3
import pandas as pd 
from modules.make_graph import graph,find_price
from modules.update_data import upd
from modules.retrieve_indicator import indicator
from datetime import date, datetime
import datetime as newdatetime
import json
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,plot,iplot

def index(request):
    template = loader.get_template('index.html')
    context = {
        'test_message' : 'working',
    }
    return HttpResponse(template.render(context, request))

def update(request,symbol):
    upd(symbol)
    return base(request,symbol)

def make_graph(cdf,analysis_type):
    x_new=[]
    y_new=[]
    x =cdf.date.values;
    for i in range(len(x)-1,-1,-1):
        x_new.append(datetime.strptime(x[i],'%d-%m-%Y'))
    y=cdf[analysis_type].values
    for i in range(len(y)-1,-1,-1):
        y_new.append(y[i])
    return x_new,y_new

def analyse(request,symbol,analysis_type='default',period=30,unit='close'):
    if analysis_type == 'default':
        analysis_type = 'SMA'
        
    template = loader.get_template('analyse.html')
    cdf1=indicator(analysis_type,symbol,period,'daily',unit)
    cdf3=indicator(analysis_type,symbol,period,'monthly',unit)
    cdf2=indicator(analysis_type,symbol,period,'weekly',unit)
    x,y=make_graph(cdf1,analysis_type)
    trace1=go.Scatter(x=x, y=y,name='daily', mode='markers', marker=dict(size=3))
    x,y=make_graph(cdf2,analysis_type)
    trace2=go.Scatter(x=x, y=y,name='weekly', mode='markers', marker=dict(size=3))
    x,y=make_graph(cdf3,analysis_type)
    trace3=go.Scatter(x=x, y=y,name='monthly', mode='markers', marker=dict(size=3))
    data =[trace1,trace2,trace3]
    plot(data,validate=True, output_type='file', include_plotlyjs=True, filename='static/analysis/temp-plot.html',auto_open=False,)
    context = {
        'test_message' : 'working',
        'symbol':symbol,
        'analyse':analysis_type,
        'period':period,
        'unit':unit,
    }
    return HttpResponse(template.render(context, request))



def base(request,symbol):
    template = loader.get_template('base.html')
    cnx = sqlite3.connect('db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM mainapp_"+symbol.lower(), cnx)
    x_date ={}
    for i in range(len(df['price_date'])):
        key =str(i)
        x_date[key]=df['price_date'][i]
    json_data = json.dumps(x_date)
    with open('static/data.json', 'w') as outfile:
        json.dump(json_data, outfile)



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
        'close':list(df['close_price'].values),
        'open':list(df['open_price'].values),
        'high':list(df['high_price'].values),
        'low':list(df['low_price'].values),
    }
    return HttpResponse(template.render(context, request))

def predict(request,symbol):
    template = loader.get_template('predict.html')
    cnx = sqlite3.connect('db.sqlite3')
    df = pd.read_sql_query("SELECT * FROM mainapp_"+symbol.lower(), cnx)
    df.price_date =pd.to_datetime(df.price_date)
    df = df.sort_values('price_date')
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