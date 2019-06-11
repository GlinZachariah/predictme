from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import sqlite3
import pandas as pd 
from modules.make_graph import graph,find_price
from modules.update_data import upd
from modules.retrieve_indicator import indicator
from modules.finalfn import gen_weight
from modules.update_db_tweet import updateTweet
from datetime import date, datetime
import datetime as newdatetime
import json
import itertools
import plotly.graph_objs as go
import plotly.offline
from plotly.offline import download_plotlyjs,plot,iplot
from yahoo_fin import stock_info as si

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
    liveval = si.get_quote_table(symbol)
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
    change = last_price -secondlast_price 
    sign=0
    if(change>0):
        sign=1
    per  = (change/last_price)*100
    change ='%.2f'%(change)
    per ='%.2f'%(per)
    if change[0] != '-' :
        change="+"+change
    last_price ='%.2f'%(last_price)
    context = {
        'symbol' : symbol,
        'sign':sign,
        'temp':df,
        'change': change,
        'last_price': last_price,
        'per':per,
        'close_date':close_date,
        'close':list(df['close_price'].values),
        'open':list(df['open_price'].values),
        'high':list(df['high_price'].values),
        'low':list(df['low_price'].values),
        'val1':liveval['1y Target Est'],
        'val2':liveval['52 Week Range'],
        'val3':liveval['Ask'],
        'val4':liveval['Avg. Volume'],
        'val5':liveval['Beta (3Y Monthly)'],
        'val6':liveval['Bid'],
        'val7':liveval['EPS (TTM)'],
        'val8':liveval['Earnings Date'],
        'val9':liveval['Ex-Dividend Date'],
        'val10':liveval['Forward Dividend & Yield'],
        'val11':liveval['Market Cap'],
        'val12':liveval['Open'],
        'val13':liveval['PE Ratio (TTM)'],
        'val14':liveval['Previous Close'],
        'val15':'%.2f'%(liveval['Quote Price']),
        'val16':liveval['Volume'],
        }
    return HttpResponse(template.render(context, request))

def predict(request,symbol):
    template = loader.get_template('predict.html')
    cnx = sqlite3.connect('db.sqlite3')
    df = pd.read_sql_query("SELECT price_date,close_price FROM mainapp_"+symbol.lower()+" ORDER by price_date DESC LIMIT 9", cnx)
    df.price_date =pd.to_datetime(df.price_date)
    df = df.sort_values('price_date')
    # df.price_date=df['price_date'].strptime("%Y-%m-%d")
    df['price_date'].apply(lambda x: x.strftime('%dY-%m-%d'))
    dates =df['price_date'].values

    prices=list(df['close_price'].values)
    arima = open('arima_'+symbol.lower()+'.txt','r')
    arima_data =arima.read()
    lstm = open('lstm_'+symbol.lower()+'.txt','r')
    lstm_data= lstm.read()
    last_date= dates[8]
    last_date=last_date.astype('M8[D]').astype('O')
    last_date += newdatetime.timedelta(days=1)
    dates =list(map(lambda x:x.astype('M8[D]').astype('O'),dates))
    val =list(map(lambda x:x.strftime("%Y-%m-%d"),dates))    
    dates=list(dates)
    dates.append(last_date)
    

    trace1 = go.Scatter(
    x = dates,
    y = prices,
    mode = 'lines',
    name ='PAST DATA'
    )

    trace2 = go.Scatter(
    x = [last_date],
    y = [arima_data],
    mode = 'markers',
    name ='ARIMA'
    )

    trace3 = go.Scatter(
    x = [last_date],
    y = [lstm_data],
    mode = 'markers',
    name ='LSTM'
    )
    data = [trace1,trace2,trace3]
    # print(data)
    layout = go.Layout(
    title="Predicted "+symbol,
    font=dict(family='Veranda', size=24, color='#7f7f7f')
    )
    fig = go.Figure(data=data,layout=layout)
    plotly.offline.plot(fig, filename = 'static/data.html', auto_open=False)

    context = {
        'symbol' : symbol,
        'temp':df,
        'dates': dates,
        'arima': arima_data,
        'lstm':lstm,
        'prices':prices,
    }
    return HttpResponse(template.render(context, request))


def twitter(request,symbol):
    template = loader.get_template('twitter.html')
    # cnx = sqlite3.connect('db.sqlite3')
    # cdf = pd.read_sql_query("SELECT * FROM mainapp_twitter_"+symbol.lower()+" ORDER by tweet_id LIMIT 1", cnx)
    # from_date =cdf['tweet_date'][0]
    from_date='2019-06-09'
    mdf=updateTweet(from_date,symbol)
    df= mdf.tail(15)
    # cnx = sqlite3.connect('db.sqlite3')
    # df = pd.read_sql_query("SELECT * FROM mainapp_twitter_"+symbol.lower()+" LIMIT 20", cnx)
    twid =list(df['Id'])
    twtext =list(df['Text'])
    twdate =list(df['Date'])
    twfollower_count =list(df['Followers count'])
    lst = []
    for i in twtext:
        if i[0:5] == "'rt :":
            lst.append(1)
        else:
            lst.append(0)
    final_items= list(zip(twid,twtext,twdate,twfollower_count,lst))
    
    
    context = {
        'test_message' : 'working',
        'symbol' : symbol,
        'final_items':final_items,
        'lst':lst,
    }
    return HttpResponse(template.render(context, request))

def news(request,symbol):
    template = loader.get_template('news.html')
    context = {
        'test_message' : 'working',
        'symbol' : symbol,
    }
    return HttpResponse(template.render(context, request))

def generateWeighted(request,symbol):
    cnx = sqlite3.connect('db.sqlite3')
    cond_df = pd.read_sql_query("SELECT * FROM mainapp_predictdata_"+symbol.lower()+" ORDER by price_date DESC LIMIT 1", cnx)
    cond_date=cond_df['price_date'][0] 
    stock_df = pd.read_sql_query("SELECT * FROM mainapp_"+symbol.lower()+" WHERE price_date> '"+cond_date+"'", cnx)
    df = gen_weight(cond_date,symbol,stock_df)
    # we = gen_weight(cond_date,symbol,stock_df)
    twdate =list(df['price_date'])
    open_p =list(df['open_price'])
    low_p =list(df['low_price'])
    close_p=list(df['close_price'])
    high_p =list(df['high_price'])
    adj_close_p=list(df['adj_close_price'])
    vol =list(df['volume'])
    senti =list(df['sentiment'])
    w_close_p =list(df['weighted_close_price'])
    adj_w_close_p = list(df['weighted_adj_close_price'])

    final_content= list(zip(twdate,open_p,close_p,high_p,low_p,vol,adj_close_p,senti,w_close_p,adj_w_close_p))
    cursor = db.cursor()
    for a,b,c,d,e,f,g,h,i,j in final_content:
        cursor.execute('''INSERT INTO mainapp_predictdata_'''+symbol.lower()+''' (price_date, open_price, close_price, high_price,low_price,volume,adj_close_price,sentiment,weighted_close_price,weighted_adj_close_price) VALUES('''+str(a)+''','''+b+''','''+c+''','''+d+''','''+e+''','''+f+''','''+g+''','''+h+''','''+i+''','''+j+''')''')
    db.commit()
    return predict(request,symbol)
    
def generateCSV(request,symbol):
    cnx = sqlite3.connect('db.sqlite3')
    print_df = pd.read_sql_query("SELECT price_date, open_price, close_price, high_price,low_price,volume,adj_close_price,sentiment,weighted_close_price,weighted_adj_close_price FROM mainapp_predictdata_"+symbol.lower(), cnx)
    # print("df sucess",print_df)
    print_df.to_csv("final_data_"+symbol.lower()+".csv",sep=",")
    return predict(request,symbol)