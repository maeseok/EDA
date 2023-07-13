import pandas as pd
import numpy as np

data = [[[1,10],[2,20]]]
col = ['A','B']
df = pd.DataFrame(data=data,columns=col)
#df.insert(3,'col4',[10,11,12])
#df.pop('col1')
#df2=df.copy(deep=False)
#df2=df.drop(labels='row1',axis=0)
#df=df.append(df2,sort=True,ignore_index=True)
#df=df.truncate(before='col2',after='col2',axis=1)
#df=df.drop_duplicates(subset='col2')
#print(df.squeeze())
#print(df.pivot(index='A',columns='B',values='C'))
#df2=df.pivot_table(index='A',columns='B',values='C',aggfunc=np.sum,sort=True)
#print(df.melt(id_vars='A',value_vars=['B','C']))
#print(df.assign(C=lambda x:x.B+5))
#print(df.replace(to_replace=1, value=3))
print(df.explode(column=['A','B']))