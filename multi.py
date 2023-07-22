import pandas as pd
import numpy as np
data = {'col1':[0,1,2,3,4], 'col2':[5,6,7,8,9],
        'row1':['A','A','A','B','B'],
        'row2':['X','X','Y','Y','Z'],
        'row3':['a','b','b','c','d']}
df = pd.DataFrame(data=data)
df = df.set_index(['row1', 'row2', 'row3'])
#print(df.xs(key=('B','Y')))
#df=(df.stack())
print(df)
#print(df.unstack())
#print(df.swaplevel(0))
print(df.droplevel(axis=0, level=1))