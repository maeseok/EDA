import pandas as pd
import numpy as np

idx = ['row1','row2']
col = ['col1','col2']
data= [['A','B'],[1,2]]
df = pd.DataFrame(data, idx, col)
idx = ['row0','row2']
col = ['col1','col2']
data= [['a','b'],[10,20]]
df2 = pd.DataFrame(data, idx, col)
#print(df)
#print(df.swapaxes(axis1=0,axis2=1))
#print(df.rename(index={'row1':'ROW1','row2':'ROW2'}))
#print(df.rename_axis(index='TEST2',columns='TEST'))
#print(df.set_index(keys='col1',append=True))
#print(df.set_axis(labels=['ROW1','ROW2'],axis=0))
#print(df.add_suffix('_TEST'))
#print(df.add_prefix('TEST_'))
#print(df.reindex(columns=['col1','col2','idx'],method='ffill'))
#print(df.reindex_like(other=df2,method='bfill'))
print(df.reset_index(drop=True))