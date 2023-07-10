import pandas as pd
import numpy as np
col = ['col1','col2','col3']
row = [10,30,50]
df = pd.DataFrame(data=[[5,pd.NA,2],
                        [5,np.nan,7],
                        [3,-5,6]],index=row, columns=col)
print(df.asof(where=[10,30,50],subset='col3'))