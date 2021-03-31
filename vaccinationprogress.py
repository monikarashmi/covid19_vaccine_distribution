import pandas as pd
df=pd.read_csv('country_vaccinations.csv')
#print(df.columns)
df2=df[['country','people_vaccinated', 'people_fully_vaccinated','date']]
#date=df['date']
#df2['date']= date
#print(df2)
#print(df2.head())
#print(df2.isnull())
#df2.dropna()
#print(df2.nunique())
df_sum=df2.groupby('country')['people_vaccinated'].sum().reset_index(name ='Total_people_vaccinated')

df_sort=df_sum.sort_values(by='Total_people_vaccinated', ascending=False)
#print(df_sort.head(10))
result=df_sort.to_csv(r'Result3.csv')