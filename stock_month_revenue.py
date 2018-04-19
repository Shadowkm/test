#coding=utf-8
import datetime
from crawlPriceP import crawlPrice 
import crawlPriceP
import requests
from io import StringIO
import pandas as pd
import numpy as np
import talib
import matplotlib.pyplot as plt
from pandas import DataFrame 
import mpl_finance
from mpl_finance import candlestick_ohlc,candlestick2_ohlc
from matplotlib import colors as mcolors, verbose, get_cachedir
from matplotlib.dates import date2num
from matplotlib.cbook import iterable, mkdirs
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.lines import Line2D, TICKLEFT, TICKRIGHT
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D
from matplotlib import axes
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import random
import plotly.plotly as py
import plotly.graph_objs as go
import pandas_datareader.data as web
import talib
import numpy
from matplotlib import dates
import datetime
from crawlPriceP import crawlPrice 
import crawlPriceP
import requests
from io import StringIO
import pandas as pd
import numpy as np
import time
from pandas.io.json import json_normalize
import math
from business_calendar import Calendar
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU,WeekdayLocator
from pandas import DatetimeIndex
from numpy import NaN
from pandas import Series
from cal_kd_rsi_2 import calculate_KD__RSI
#coding=utf-8




def  monthly_report(year,month) :
    #year=103
    #month=1
    # 假如是西元，轉成民國
    if year > 1990:
        year -= 1911
    year_str=str(year)
    month_str=str(month)
    date_file = datetime.datetime(2016,6,24)
    Y_0_str=str(date_file .year)
    M_0_str=str(date_file .month) if date_file .month >9 else '0'+str(date_file .month)
    D_0_str=str(date_file .day) if date_file .day>9 else '0'+str(date_file .day)
    #print Y_0_str
    date_0 = Y_0_str+M_0_str+D_0_str
    delete_row=0
    N=range(1,delete_row)
    file_name4='D:\Python27\Taiwan_stock_data_daily\VOHLC\Close_data_%s.csv' % date_0
    close_0= pd.read_csv(file_name4,parse_dates=True ,index_col = 0,header=0, skiprows=N , encoding='big5')
    
    #close.shape[0]
    #print 'close_0.index',close_0
    length_row=close_0.shape[0]
    length_col=close_0.shape[1]
    length_calcu=length_col
    close= pd.read_csv(file_name4,parse_dates=True , skiprows=N ,skipfooter=length_row-1,index_col = 0, usecols=range(length_col),header=0 ,engine='python', encoding='big5')
    close_name=list(close.columns.values)
    #print length_calcu
    #print '25,',close_name,close_name[len(close_name)-1]
    
    # 下載該年月的網站，並用pandas轉換成 dataframe
    month_price0=[]
    closename_str_big=[]
    html_df = pd.read_html('http://mops.twse.com.tw/nas/t21/sii/t21sc03_'+str(year)+'_'+str(month)+'_0.html')    
    # 處理一下資料
    #for i in range(length_calcu):
    #
    m=0
    i=0
    while i !=len(close_name):
        n=0 
        print i
        # m代表第幾張圖表
        closename_str=str(close_name[i])
        #print 'df',df,'df[n]',df[n],'html_df[0]',html_df[0],'html_df[1]',html_df[1],'html_df[2]',html_df[2]
        #df = df[list(range(0,10))]
        #print 'closename_str', closename_str,'closename_str'
        #print df[n] == closename_str,'df[n] == closename_str'
        #print df.index,'df.index'
        try:
            df = html_df[m].copy()
            df= df[list(range(10))]
            column_index = df.index[(df[n] == closename_str)][0]
            print "this is",m
            print 'df.index',df.index,' df.index[(df[n] ]'
            print 'column_index',column_index
            #df.columns = df.iloc[column_index]
            print 'df.columns',df.columns
            #print 'df當月營收',df['當月營收'] 
            #df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
            month_price=pd.to_numeric(df.iat[column_index,2])#thousand unit
            month_price0.append(month_price)
            closename_str_big.append(closename_str)
            month_price_ts=pd.Series(month_price0,index=[closename_str_big])
            #print  'dfiat', month_price,'type',type(month_price)
            #df = df[~df['當月營收'].isnull()]
            #df = df[df['2330'] != '合計']
            i=i+1
        except:
            print "next", m 
            m+=1
            i=i
        month_price_df=DataFrame(month_price_ts,columns=['month_revenue'])
        #print month_price_df
        file_name6 ='D:\Python27\Taiwan_stock_data_daily\VOHLC\month_revenue\month_price_%s_%s.csv' % (year_str ,month_str)
        month_price_df.to_csv(file_name6)

        if m==62 and  i!=close_name[len(close_name)-1]:
            month_price_ts=pd.Series(0,index=[closename_str_big])
            m=0
            i=i+1
        #column_index=df.index
        
            #AB=(df[n] == '1102')
    


    close= pd.read_csv(file_name4,parse_dates=True , skiprows=N ,skipfooter=length_row-1,index_col = 0, usecols=range(length_col),header=0 ,engine='python', encoding='big5')
    close_name=list(close.columns.values)
    file_name6 ='D:\Python27\Taiwan_stock_data_daily\VOHLC\month_price_%s_%s.csv' %  (year_str ,month_str)
    month_price_df.to_csv(file_name6)






if __name__ == '__main__':
    year=list(range(104))
    month=range(1,13)
    for i in range(len(year)):
        for j in month:
            print year[i],j
            monthly_report(year[i],j)








