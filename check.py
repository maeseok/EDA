import pandas as pd
import numpy as np

n=np.NaN
idx =  ['row1','row2','row3']
col =  ['col1','col2','col3']
data = [[1,2,10],[1,5,12],[1,2,4]]
df = pd.DataFrame(data,idx,col)
#df1 = pd.DataFrame([True],['row'],['col'])
#df2 = pd.DataFrame(data=[[False],[3,2]])
#df=df.iloc[:2]
#print(df.infer_objects().dtypes)
#df=df.isin([1,2])
#print(df.any())
#print(df.count())
#rint(df1.equals(df2))
#print(df1.bool())
print(df)
print(df.duplicated(subset=['col1','col2']))