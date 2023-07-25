import pandas as pd
import numpy as np
data = {'col1':[1,2],'col2':[3,4]}
df = pd.DataFrame(data = data)
print(df)
#df=df.__iter__()
#print(list(df))
#df=df.items()
'''for i in df:
    for j in i:
        print(j)
df=df.iterrows()
for i in df:
    for j in i:
        print(j)'''
df=df.itertuples()
print(list(df))