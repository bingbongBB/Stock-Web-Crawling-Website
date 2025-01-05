from django.db import models


# Create your models here.
class StockHistory(models.Model): 
    code=models.IntegerField(blank=True,null=True)
    name=models.CharField(max_length=20,blank=True,null=True)
    data = models.DateTimeField(blank=True,null=True)       #時間
    capacity = models.IntegerField(blank=True,null=True)    #總成交股數
    turnover = models.IntegerField(blank=True,null=True)    #總成交金額
    open = models.FloatField(blank=True,null=True)          #開盤價
    high = models.FloatField(blank=True,null=True)          #盤中最高價
    low = models.FloatField(blank=True,null=True)           #盤中最低價
    close = models.FloatField(blank=True,null=True)         #收盤價
    change = models.FloatField(blank=True,null=True)        #漲跌價差
    transaction = models.IntegerField(blank=True,null=True) #成交筆數

class PicAdd(models.Model):
    date = models.CharField(max_length=20,blank=True,null=True)   #時間
    company = models.CharField(max_length=50,blank=True,null=True)#公司
    mode = models.CharField(max_length=20,blank=True,null=True)   #型式
    address = models.CharField(max_length=70,blank=True,null=True)#位址


