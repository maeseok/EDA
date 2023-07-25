import pandas as pd
import numpy as np
#객체 간 연산
#원본 데이터
data=[[1.25,2.23],[3.21,4.56]]
col=['col1','col2']
row=['row1','row2']
df = pd.DataFrame(data=data, index=row, columns=col)
#print(df)
#덧셈
#df=df.add(1)

#df2=pd.DataFrame(data=[[1],[2],[3]],index=['row4','row5','row6'],columns=['col1'])
#df=df.add(df2)

#df=df.add(df2,fill_value=0)
#print(df)

#곱셈
#df=df.mul(2)

#df2=pd.DataFrame(data=[[1],[3],[5]],index=['row4','row5','row6'],columns=['col1'])
#df=df.mul(df2,fill_value=0)
#print(df)

#나머지
#df=df.mod(2)

#df2=pd.DataFrame(data=[[2],[2],[2]],index=['row4','row5','row6'],columns=['col1'])
#df=df.mod(df2,fill_value=1)
#print(df)

#df1=pd.DataFrame(data=[[1,2],[3,4]])
#df2=pd.DataFrame(data=[[5,6],[7,8]])
#df=df1.dot(df2)
#print(df)

#---------------------------------------
#객체 내 연산
#print(df.round(1))
#print(df.sum(axis=0))

#전치
#print(df.transpose())

#data = [[5],[5],[pd.NA],[1],[-3.1],[6],[0.1],[-3],[3]]
#row = ['A','B','C','D','E','F','G','H','I']
#df = pd.DataFrame(data=data, index=row, columns=['Value'])

#df['min']=df['Value'].rank(method='min')


#a = [1,2,3,4,5,6,7,8]
#b = [8,7,6,5,4,3,2,1]
#c = [1,2,4,8,16,32,64,128]
#data = {"col1":a,"col2":b,"col3":c}
#df = pd.DataFrame(data)
#df=df.diff(axis=0)
#df=df.pct_change()
#df=df.expanding().sum()'
#df=df.rolling(window=3).sum()

idx=['A','A','B','B','C','C','D','D','E','E']
col=['col1','col2','col3']
data = np.random.randint(0,9,(10,3))
df = pd.DataFrame(data=data, index=idx, columns=col).reset_index()
df=df.groupby('index').mean()
print(df)

