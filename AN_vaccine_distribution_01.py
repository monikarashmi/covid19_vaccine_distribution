import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
df=pd.read_csv('country_vaccinations.csv')
#print(df.columns)
#print(df.head())
#print(df.tail())
print(df['vaccines'].unique())
df.drop_duplicates(subset ="vaccines", keep = False, inplace = True) 

#print(df.sort_values("vaccines", inplace=True) )
#print(df['country'].nunique())


#df = df.groupby(['country', 'vaccines']).size()
#print (df)
#filter1=df["vaccines"]=='Sputnik V'
#print(filter1)
#print(df.where(filter1, inplace = True) )
#print(df['country'])

if df['vaccines'] == 'Pfizer/BioNTech'
          print(df['country'])
 #else: 
     print('dkdkdk')
     #print('country not found')
