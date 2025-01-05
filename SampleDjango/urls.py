"""SampleDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from sampleApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('realtime/',views.realtime),
    path('home/',views.home,name="home"),
    path('stocksearch/',views.stocksearch,name="stocksearch"),
    path('stocknowsearch/',views.stocknowsearch,name="stocknowsearch"),
    re_path('stockhistory/(?P<stock>[0-9]{0,4})/(?P<year>[0-9]{0,4})/(?P<month>[0-9]{0,2})',views.stockhistory),
]
