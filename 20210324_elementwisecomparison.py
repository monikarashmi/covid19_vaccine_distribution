import pandas as pd
#import numpy as np
#import matplotlib.pyplot as mlt
df=pd.read_csv('country_vaccinations.csv')
#print(df['vaccines'].unique())
#df1= df.head(700)
df2=df[['country','vaccines']]

for index, row in df2.iterrows():
    #print('you are inside for loop')
    #print(df2[['country','vaccines']])
    print('df2 is printed above')
    df3=df2[['country','vaccines']]
    df4=df3.drop_duplicates(subset=None, keep='first', inplace=False)
    #print(df4)
    print('exit for loop')
result=df4.to_csv(r'Result2.csv')
print('result is stored in csv')
