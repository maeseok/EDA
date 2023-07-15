import pandas as pd
import numpy as np

data = [['A',2,3],['B',5,pd.NA],['A',2,6]]
index = ['row1','row2','row3']
columns=['col1','col2','col3']
df= pd.DataFrame(data=data, index=index, columns=columns)
print(df)
print(df.nunique(axis=0,dropna=False))