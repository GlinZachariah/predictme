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
    graph(symbol,df)
    secondlast_price,last_price =find_price(symbol,df)
    change = secondlast_price -last_price
    last_price ="{0:.2f}".format(last_price)
    context = {
        'symbol' : symbol,
        'temp':df,
        'change': change,
        'last_price': last_price,
    }
    return HttpResponse(template.render(context, request))