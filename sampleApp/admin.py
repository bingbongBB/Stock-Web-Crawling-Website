from django.contrib import admin
from .models import StockHistory,PicAdd


# Register your models here.
@admin.register(StockHistory)
class StockHistoryAdmin(admin.ModelAdmin):
    list_display=('code','name','data','capacity','turnover','open','high','low','close','change','transaction')
    list_filter=('code','name','data')
@admin.register(PicAdd)
class PicAddAdmin(admin.ModelAdmin):
    list_display=('date','company','mode','address')
    list_filter=('date','company','mode')
