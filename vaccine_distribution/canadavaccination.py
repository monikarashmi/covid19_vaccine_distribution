import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
df=pd.read_csv('country_vaccinations.csv',index_col=())
df1=df[['date','country','daily_vaccinations_per_million']]
#print(df1)

print(df1.dropna())
filter1=df1['country']=="Canada","United States"
print(filter1)
df2=df1.where(df1['country']=="Canada")
#print(df2)
print(df2.dropna())
#df2=df2[1004:1094]
df2=df2.dropna()
#print(df2.describe())
df2.plot(x='date', y='daily_vaccinations_per_million', kind='line')

