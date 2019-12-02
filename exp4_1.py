import pandas as pd

data1 = {'Student':['Ice Bear','Panda','Grizzly'],'Math':[80,95,79]}
we = pd.DataFrame(data1,columns=['Student','Math']) 

data2 = {'Student':['Ice Bear','Panda','Grizzly'],'Electronics':[85,81,83]}
bare = pd.DataFrame(data2,columns=['Student','Electronics']) 

data3 = {'Student':['Ice Bear','Panda','Grizzly'],'GEAS':[90,79,93]}
bear = pd.DataFrame(data3,columns=['Student','GEAS'])

data4 = {'Student':['Ice Bear','Panda','Grizzly'],'ESAT':[93,89,88]}
s = pd.DataFrame(data4,columns=['Student','ESAT'])  

df1 = we.merge(bare,how=('right'))
df2 = df1.merge(bear,how=('right'))
df3 = df2.merge(s,how=('right'))


long_df = pd.melt(df3,id_vars=['Student'],var_name='Subject',value_name='Grades')

final_df = long_df.sort_values('Student').reset_index().drop(columns=['index'])
print(final_df)
