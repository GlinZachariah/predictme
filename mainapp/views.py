from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import TSLA
import sqlite3
import pandas as pd 
from modules.make_graph import graph


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
    context = {
        'test_message' : 'working',
        'temp':df,
    }
    return HttpResponse(template.render(context, request))