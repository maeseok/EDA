import pandas as pd
import numpy as np
col = ['col1','col2','col3']
row = ['row1','row2','row3']
data = [[1,2,3],[4,5,6],[7,8,9]]
df = pd.DataFrame(data=data,index=row,columns=col)

df=df.eval('col4=col1*col2*col3',inplace=False)
print(df)