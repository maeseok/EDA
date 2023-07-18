import pandas as pd
import numpy as np

data=[[7,5,3],[5,2,7],[10,9,8]]
index=['row1','row2','row3']
columns=['col1','col2','col3']
df=pd.DataFrame(data=data,index=index,columns=columns)
print(df)
#print(df.min(axis=1))
#print(df.mean(axis=1))
#print(df.median())
#print(df.mode())
#print(df.std())
#print(df.var())
#print(df.mad())
#print(df.cummax())
#print(df.cummin())
#print(df.cumsum())
#print(df.cumprod())
print(df.quantile(q=0.5))