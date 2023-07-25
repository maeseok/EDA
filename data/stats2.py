import pandas as pd
import numpy as np
col=['col1','col2']
data=[[2,1],[-2,4],[5,6],[-3,5]]
df = pd.DataFrame(data=data, columns=col)
print(df)
#print(df.cov())
#print(df.kurt())
#print(df.sem())
#print(df.skew())
print(df.corr(method='spearman'))