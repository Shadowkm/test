#coding=utf-8
import requests
import time
from io import StringIO
import pandas as pd
import numpy as np
def crawlPrice(date):
    r = requests.post('http://app.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php', data={
        'download': 'csv',
        'qdate':date,
        'selectType':'ALL',
    })
    r.encoding = 'big5'
    print date
    df = pd.read_csv(StringIO("\n".join([i.translate({ord(c): None for c in ' '}) 
                                         for i in r.text.split('\n') 
                                         if len(i.split('",')) == 16 and i[0] != '='])), header=0)

    time.sleep(1)
    df.set_index('證券代號', inplace=True)
    df.columns = ['證券名稱', '成交量', '成交筆數', '成交金額', '開盤價', '最高價', '最低價', '收盤價',
                  '漲跌(+/-)', '漲跌價差', '最後揭示買價', '最後揭示買量', '最後揭示賣價', '最後揭示賣量', '本益比']
    
    df['成交量'] /= 1000
    df = df.drop(['漲跌(+/-)','證券名稱','最後揭示買量','最後揭示賣量'], axis=1)
    df = df.replace('--', np.nan)
    df = df.apply(pd.to_numeric)
    df = df.apply(pd.to_numeric)
    assert len(set(df.index)) == len(df.index)
    return df
    #print date

#print crawlPrice("106/12/13")