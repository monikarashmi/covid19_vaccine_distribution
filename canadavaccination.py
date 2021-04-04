import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('country_vaccinations.csv',index_col=())
df1=df[['date','country','daily_vaccinations_per_million']]
#print(df1)
#print(df1.dropna())
filter1=df1['country']=="Canada"
print((df1.where(filter1,inplace=True))