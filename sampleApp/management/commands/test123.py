from django.core.management.base import BaseCommand
import twstock
from sampleApp.models import StockHistory
import time
import datetime

#撰寫一個新指令來存取資料，名稱叫做test123
class Command(BaseCommand):     
    def handle(self, *args, **options):
        #將10支股票存成字典
        stock_name={'台塑':'1301','南亞':'1303','鴻海':'2317','台積電':'2330','中華電':'2412','聯發科':'2454','長榮':'2603','富邦金':'2881','國泰金':'2882','台塑化':'6505'}
        
        #建立一個空字串用來儲存twstock傳給我們的即時資訊
        twstock_data = []

        #開始接收 
        print('Start')
        #對每個key-value開始跑迴圈
        for k,v in stock_name.items():
            #因為回傳過來的值是一個list，所以將他存入另一個list:everyStock中
            everyStock = twstock.Stock(v).fetch(2022,6)
            #對everyStock中的回傳值再做一次迴圈
            for stock in everyStock:
                #將回傳過來的值按照我們在models裡定義的欄位append在用來接收資料的twstock_data中
                twstock_data.append(StockHistory(code=v,name=k,data=stock.date,capacity=stock.capacity,turnover=stock.turnover,open=stock.open,high=stock.high\
                    ,low=stock.low,close=stock.close,change=stock.change,transaction=stock.transaction))
            #設定timesleep以免一次使用大量的請求而被網頁ban掉
            time.sleep(30)
        
        #將10筆股票資料導入到資料庫中
        StockHistory.objects.bulk_create(twstock_data)
        print('done')