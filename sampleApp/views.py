from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
import matplotlib.pyplot as plt
import twstock
import random
import time
from django.views.decorators.csrf import csrf_exempt
import requests
from sampleApp.models import StockHistory
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as pltg


def home(request):
    if request.method == 'GET':
        return render(request,"index.html")
def stocksearch(request):
    if request.method == 'GET':
        return render(request, "stocksearch.html")
def stockhistory(request,stock,year,month):
    if request.method == 'GET':
        day = {"01":"31","02":"28","03":"31","04":"30","05":"31","06":"30","07":"31","08":"31","09":"30","10":"31","11":"30","12":"31"}
        date = year+'-'+month
        s = StockHistory.objects.filter(data__range=[date+"-01",date+"-"+day[month]],code=stock).all().values()
        df = pd.DataFrame(list(s))
        df['data'] = pd.to_datetime(df['data']).dt.date
        month = df['data']#X軸
        open = df['open']#開盤線的資料
        close = df['close']#收盤線的資料
        open_close = plot([pltg.Scatter(x=df['data'],y=df['open'],mode="lines",line={'color':'red'},name='open')
            ,pltg.Scatter(x=df['data'],y=df['close'],mode="lines",line={'color':'blue'},name='close')
            ],output_type='div')
    
        kd = plot([pltg.Candlestick(x=df['data'],open=df['open'],high=df['high'],low=df['low'],close=df['close'],increasing_line_color='red',decreasing_line_color='green')]
            ,output_type='div')
        return render(request, "stocksearch.html", context={'open_close': open_close,'kd':kd})

def stocknowsearch(request):
    if request.method == 'GET':
        return render(request,"stocknowsearch.html")

@csrf_exempt
def realtime(request):
    stock_code = request.POST.get("stock_code")
    stock=twstock.realtime.get(stock_code)    #這裡改成需要查詢的股票
    date = datetime.fromtimestamp(stock['timestamp'])
    code = stock['info']['code']
    name = stock['info']['name']
    fullname = stock['info']['fullname']
    best_bid_price = stock['realtime']['best_bid_price']
    best_bid_volume = stock['realtime']['best_bid_volume']
    best_ask_price = stock['realtime']['best_ask_price']
    best_ask_volume = stock['realtime']['best_ask_volume']
    _open = stock['realtime']['open']
    high = stock['realtime']['high']
    low = stock['realtime']['low']
    return JsonResponse({'date':date,      #將所有值用Json回傳給前端
                        'code':code,
                        'name':name,
                        'fullname':fullname,
                        'best_bid_price':best_bid_price,
                        'best_bid_volume':best_bid_volume,
                        'best_ask_price':best_ask_price,
                        'best_ask_volume':best_ask_volume,
                        'open':_open,
                        'high':high,
                        'low':low})