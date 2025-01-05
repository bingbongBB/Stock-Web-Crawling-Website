import os,twstock,sqlite3
import pandas as pd
import time

#連結資料庫，設定將資料庫建在路徑裡
conn = sqlite3.connect('D:/Sample/SampleDjango/db.sqlite3')
#建好10支股票的list
tenStock=['1301','1303','2317','2330','2412','2454','2603','2881','2882','6505']

#1月到12月的迴圈
for j in range(1,13):
    for i in tenStock:
        #利用twstock來抓取十支股票的資訊
        everyStock = twstock.Stock(i,initial_fetch=False)
        
        #利用pandas的DataFrame來結構化股票的資料並利用fetch()來抓取該年的資料
        StockHistory = pd.DataFrame(everyStock.fetch(2021,j))
        
        #利用pandas的to_sql來將資料存到資料庫中
        StockHistory.to_sql(i,conn)
        
        #設定timesleep以免一次抓太多的物件被網頁ban掉
        time.sleep(10)
conn.commit()
conn.close()
