from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import TSLA

def index(request):
    template = loader.get_template('index.html')
    context = {
        'test_message' : 'working',
    }
    return HttpResponse(template.render(context, request))

def base(request,symbol):
    template = loader.get_template('base.html')
    context = {
        'test_message' : 'working',
        'temp':symbol,
    }
    return HttpResponse(template.render(context, request))