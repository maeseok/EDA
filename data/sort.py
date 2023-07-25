import pandas as pd
import numpy as np


n=np.NaN

df = pd.DataFrame({'A':[2,4,6],'B':[6,1,8]})
df2 = pd.DataFrame({'A':[2,7,3],'B':[1,2,3]})
#df = pd.DataFrame({'col2':['B','C','D'], 'NUM':[6,7,8]})
#df2 = pd.DataFrame({'col1':['A','B','C'], 'NUM':[2,4,5]}) 
#print(df.sort_values(by=['col1'],axis=0,ascending=True))
#print(df.sort_index(axis=0, level=0,ascending=False))
#print(df.nlargest(2,columns="col2",keep="all"))
#print(df2.combine_first(df))
#print(df.join(df2,how='right'))
#print(df.merge(df2,left_on='col2',right_on='col1'))
#print(df.align(df2,join='inner')[0])
#print(df.align(df2,join='inner')[1])
print(df)
print(df2)
df=df.update(df2,overwrite=True)
print(df)