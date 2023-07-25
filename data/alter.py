import pandas as pd
import numpy as np

df = pd.DataFrame([[1,2],[3,4]], columns=['col1','col2'],index=['row1','row2'])
data={'col1':[1,2], 'col2':[3,4]}
print(df)
#print(df.to_csv(path_or_buf='test.csv'))
#f.to_excel(excel_writer='test.xlsx',sheet_name='test')
#df.to_clipboard()
#print(df.to_dict(orient='dict'))
#print(df.to_markdown())
#df.to_pickle('test.pkl')
#print(df.to_html())
#print(df.to_string())
#print(type(df.to_string()))
df2 = pd.DataFrame.from_dict(data=data, orient='columns')
print(df2)