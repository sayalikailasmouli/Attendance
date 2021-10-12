import pandas as pd     
import plotly.express as ep 


df=pd.read_csv("cas.csv")
fig=ep.line(df,x='name',y='Phone number',color='2021-09-16,2021-09-17',title='ATTENDANCE')
fig.show()