import pandas as pd
import numpy as np

x = pd.date_range('2023-06-20',periods=5, freq='D')
#data=x.tz_convert('US/Eastern')
#x= x.tz_localize('US/Eastern')
#x= pd.period_range(start='2023-07-19 00:00:00',end='2023-07-19 01:00:00',freq='30T')
df=pd.DataFrame(data={'col1':range(len(x)),'col2':[0,0,0,0,0]}, index=x)
#print(df.at_time('06:00'))
#print(df.between_time(start_time='00:00', end_time='03:00'))
print(df)
#print(df.first('4D'))
#print(df.last('4D'))
#print(df.to_timestamp(freq="T", how='start'))
#print(df.asfreq(freq='30S',method='bfill'))
#print(df.resample(rule='3T',label='left').sum())
#print(df.shift(periods=1,axis=1))
print(x.to_period("D"))