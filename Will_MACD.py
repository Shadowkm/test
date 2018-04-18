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





def calculate_KD__RSI(stock_num,YYYY,MM,DD,day,week,delete_row):
	stock_num=stock_num
	date_file_lastest= datetime.datetime.now()
	time4= datetime.datetime.now()
	Y=str(YYYY)
	M=str(MM)
	D=str(DD)
	day=day #default to be True
	week=week #default to be False
	Y_1='1111'
	M_1='11'
	D_1='11'
	#while Y_1!=Y or M_1!=M or D_1!=D :
	#	Y_1=str(time4.year)
    #	M_1=str(time4.month) if time4.month >9 else '0'+str(time4.month)
    #	D_1=str(time4.day) if time4.day>9 else '0'+str(time4.day)
    #	time4=time4-datetime.timedelta(days=1)
    # 	days=days+1
	n_days=10


	time = datetime.datetime.now()


	delete_row=delete_row

	date_file = datetime.datetime(2016,06,24)
	#print date_file
	Y_0_str=str(date_file .year)
	M_0_str=str(date_file .month) if date_file .month >9 else '0'+str(date_file .month)
	D_0_str=str(date_file .day) if date_file .day>9 else '0'+str(date_file .day)

	#print Y_0_str
	date_0 = Y_0_str+M_0_str+D_0_str
	#print date_0


	stock_number=str(stock_num)
	file_name1='D:\Python27\Taiwan_stock_data_daily\VOHLC\Open_data_%s.csv' % date_0
	file_name2='D:\Python27\Taiwan_stock_data_daily\VOHLC\High_data_%s.csv' % date_0
	file_name3='D:\Python27\Taiwan_stock_data_daily\VOHLC\Low_data_%s.csv' % date_0
	file_name4='D:\Python27\Taiwan_stock_data_daily\VOHLC\Close_data_%s.csv' % date_0
	file_name5='D:\Python27\Taiwan_stock_data_daily\VOHLC\Volume_data_%s.csv' % date_0
	file_name6='D:\Python27\Taiwan_stock_data_daily\VOHLC\All_OHLC_data_%s.csv' % date_0


	N=range(1,delete_row)
	close= pd.read_csv(file_name4,parse_dates=True ,index_col = 0,header=0, skiprows=N , encoding='big5')
	volume=pd.read_csv(file_name5,parse_dates=True ,index_col = 0,header=0, skiprows=N , encoding='big5')
	openv=pd.read_csv(file_name1,parse_dates=True ,index_col = 0,header=0, skiprows=N , encoding='big5')
	high=pd.read_csv(file_name2,parse_dates=True ,index_col = 0,header=0,skiprows=N , encoding='big5')
	low=pd.read_csv(file_name3,parse_dates=True ,index_col = 0, header=0,skiprows=N , encoding='big5')
	standard=pd.read_csv(file_name3,parse_dates=True ,usecols=(0,0), header=0,skiprows=N , encoding='big5')




	#standard=standard.resample('W', how='mean', closed='right', label='right')


	MA_10=close.rolling(window=100,min_periods=0).mean()
	#print "MA_10",len(MA_10)











	if week==1:
		# weekly data transform 
		close=close.resample('W', how='mean', closed='right', label='right')
		#print "tsmc_week",close
		volume=volume.resample('W', how='mean', closed='right', label='right')
		#print "tsmc_week",volume
		openv=openv.resample('W', how='mean', closed='right', label='right')
		#print "tsmc_week",openv
		high=high.resample('W', how='mean', closed='right', label='right')
		#print "tsmc_week",high
		low=low.resample('W', how='mean', closed='right', label='right')
		#print 'close',close,close.shape[0]





	#print '111111' ,n_days

	tsmc={'open':openv[stock_number].dropna().astype(float),
		'high':high[stock_number].dropna().astype(float),
		'low':low[stock_number].dropna().astype(float),
		'close':close[stock_number].dropna().astype(float),
		'volume':volume[stock_number].dropna().astype(float),
		}


	array_ohlc=pd.DataFrame({'open':tsmc['open'],'high':tsmc['high'],'low':tsmc['low'],'close':tsmc['close']})
	#print array_ohlc,'array_ohlc'
	array_high=np.array(tsmc['high'])
	array_low=np.array(tsmc['low'])
	array_close=np.array(tsmc['close'])
	array_standard=np.array(standard)
	#print len(array_standard)

	#計算KD指標
	Numerator=array_ohlc['close']-array_ohlc['low'].rolling(window=9).min()
	Denumerator=(array_ohlc['high'].rolling(window=9).max() - array_ohlc['low'].rolling(window=9).min())
	#print 'array_ohlc[].rolling(window=9).min()',Numerator,Denumerator

	data_K9=[50]
	data_D9=[50]
	#data_K9.append(50)

	Rev=100*Numerator/Denumerator
	#print type(Rev)


	Rev= Rev.fillna(value=50)
	#print Rev




	WILLR_5 = WILLR(high=array_high, low=array_low, close=array_close, timeperiod=5)
	WILLR_10 = WILLR(high=array_high, low=array_low, close=array_close, timeperiod=10)
	print WILLR_5,WILLR_10
	exit()
	#Rev = Rev[~numpy.isnan(Rev)]



	M= len(close)-len(Rev)-1+len(N)
	M_rsi=len(close)-len(array_standard)+len(N)



	#print 'array_standard',array_standard,len(array_standard)
	#使用pd.to_datetime可以解決index變成datetime的問題
	my_data = pd.read_csv(file_name1, usecols=(0,0), header=0, skiprows=M,encoding='big5') 
	my_data_date = pd.read_csv(file_name1 ,usecols=(0,0), index_col = 0,header=0, skiprows=M,encoding='big5') 

	#print my_data,my_data_date

	# transfter to the date, week ,month,quater
	mydata_array=np.matrix(my_data)
	#print 'rev',Rev,len(Rev),len(mydata_array_rsi)
	#print len(mydata_array)
	my_data_date=pd.to_datetime(my_data_date.index,format='%Y-%m-%d') #把index轉換成datetime

	#print my_data_date,type(my_data_date),len(my_data_date)


	M_del= len(close)-len(Rev)

	standard_week=pd.to_datetime(close.index,format='%Y-%m-%d') #把index轉換成datetime

	#print len(standard_week)

	##pd.DatetimeIndex.delete(standard_week)
	#print standard_week,len(standard_week)



	#print len(stand_D)

	#Rev.where(Rev.notnull(), 50)

	# MA移動平均線=100 

	#計算KD指標
	for i in range(len(Rev)-1):
		K9_value =Rev[i]*1/3 + data_K9[i]*2/3
  		data_K9.append(K9_value)
	# 	print 'data_K9',K9_value,data_K9
  	 	D9_value =  data_D9[i-1]*2/3 +data_K9[i]*1/3
 		data_D9.append(D9_value)

	#print Rev,len(Rev),data_K9,len(data_K9)

	#print 'length would be  ', array_high.shape[0],len(array_low),len(array_close),array_high,array_low

	slowk, slowd = talib.STOCH(high=array_high,low=array_low,close=array_close,
	fastk_period=9,slowk_period=3,slowk_matype=0,slowd_period=3,
	slowd_matype=0)
	#print slowk, "slowk",len(slowk)
	#print slowd, "slowd",len(slowd)

	length_rsi=len(slowk)

	for i in range(len(slowk)):
		if np.isnan(slowk[i]):
			slowk[i]=50
			#print 'i in if',i
		else:
			slowk[i]=slowk[i]

	for i in range(len(slowd)):
		if np.isnan(slowd[i]):
			slowd[i]=50
			#print 'i in if',i
		else:
			slowd[i]=slowd[i]

	#slowk = slowk[~numpy.isnan(slowk)]
	#slowd =slowd[~numpy.isnan(slowd)]
	#print slowk

	#print 'shape',len(slowd)


	#計算RSI值

	my_data_rsi= pd.read_csv(file_name1, usecols=(0,0), index_col = 0, header=0, skiprows=M_rsi,encoding='big5') 



	mydata_array_rsi=np.matrix(my_data_rsi)
	#print array_close,len(array_close),tsmc['close']

	my_data_rsi=pd.to_datetime(my_data_rsi.index,format='%Y-%m-%d') #把index轉換成datetime


	real_5=talib.RSI(array_close,timeperiod=5)
	real_10=talib.RSI(array_close,timeperiod=10)


	#real_5= real_5.fillna(value=50)
	#real_10=real_10.fillna(value=50)
	#real_5.where(real_5.notnull(), 50)
	#real_5= real_5.replace("nan",int(3))
	for i in range(len(real_5)):
		if np.isnan(real_5[i]):
			real_5[i]=50
			#print 'i in if',i
		else:
			real_5[i]=real_5[i]

	for i in range(len(real_10)):
		if np.isnan(real_10[i]):
			real_10[i]=50
			#print 'i in if',i
		else:
			real_10[i]=real_10[i]


	#print real_5,real_10





	#print standard_week,len(standard_week),real_5,len(real_5)


	#計算KD+RSI大於170
	data_KD_RSI_170=np.array(data_K9)+np.array(real_5)
	#print data_KD_RSI_170
	#print len(data_KD_RSI_170),data_KD_RSI_170
	array_date=np.array(my_data)

	#print 'array_date',tsmc['close']

	n=0
	m=[]
	the_dates_KD_RSI_170=[]
	while n !=(len(data_KD_RSI_170)):
		if data_KD_RSI_170[n]>170:
			m.append(n)
			the_dates_KD_RSI_170.append(standard_week[n])
			#print n

		n=n+1
	#print 'mmmmmmmm',the_dates_KD_RSI_170,'nnnnnnnnnn',n
	#print my_data
	#print the_dates_KD_RSI_170
	print the_dates_KD_RSI_170

	date_170=[]
	
	#date_170=pd.DataFrame({stock_number:the_dates_KD_RSI_170})
	#the_dates_KD_RSI_170 = the_dates_KD_RSI_170.localtime(timestamp)
	#the_dates_KD_RSI_170 = pd.to_string(the_dates_KD_RSI_170)
	#date_170=pd.DataFrame({stock_number:the_dates_KD_RSI_170})
	#date_170=pd.datetime(date_170)
	#date_170.set_index(the_dates_KD_RSI_170)

	#print 'date_170',date_170
	#, format='%Y%m%d', errors='ignore'
	#print  type(date_170),'222',date_170,'111',type(date_170[0]),date_170[0]
	return the_dates_KD_RSI_170


	
	plt.style.use('ggplot')

	ax1= plt.subplot2grid((10,1),(5,0),rowspan=5,colspan=1)
	ax2= plt.subplot2grid((6,1),(1,0),rowspan=2,colspan=1,sharex=ax1)
	#print dates_week1,slowk

	#slowk,slowd 使用TA-lib去做計算

	#ax2.plot(dates_week2,slowk, '-', color='b')
	#ax2.plot(dates_week2,slowd, '-', color='orange')
	#print len(dates_week1)
	#print my_data_date
	#data_K9,data_D9 使用標準公式計算，與yahoo走勢相同
	#ax1.plot(my_data_date,data_K9, '-', color='b')
	#ax1.plot(my_data_date,data_D9, '-', color='orange')
	ax2.plot(standard_week,real_5, '-', color='black')
	ax2.plot(standard_week,real_10, '-', color='red')
	ax1.plot(standard_week,data_K9, '-', color='b')
	ax1.plot(standard_week,data_D9, '-', color='orange')


	#dayFormatter = dates.DateFormatter('%Y-%m-%d')
	#ax1.xaxis.set_major_formatter(dayFormatter) 

	#plt.show()


if __name__ == '__main__':
	calculate_KD__RSI(2303,2017,12,01,1,1,100)
