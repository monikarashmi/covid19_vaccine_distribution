import pandas as pd
df=pd.read_csv('country_vaccinations.csv')
#print(df)
df2=df[['country','total_vaccinations_per_hundred', 'people_vaccinated_per_hundred'
            ,'people_fully_vaccinated_per_hundred','date']]

#print(df2.head(5))
#print(df2.isnull())
#df2.dropna()
#print(df2.nunique())
#print(df2['total_vaccinations_per_hundred'])
#print(Final_Result1)

#print(Final_Result2)
#Final_Result2.to_csv(r'Result5.csv')
x1='people fully vaccinated per hundred'
x2='people vaccinated per hundred'

#asking for user input
input1=input('Enter whether you want to know people fully vaccinated per hundred or people vaccinated per hundred:')
print(input1)
if input1== x1 :
    result1=df2.groupby('country')['people_fully_vaccinated_per_hundred'].sum().reset_index(name ='Total_percent of people_fully vaccinated')
    #print(result1)
    Final_Result1=result1.sort_values(by='Total_percent of people_fully vaccinated', ascending=False)
    Final_Result1.to_csv(r'Result4.csv')
    print(Final_Result1)
elif input1== x2 :
    result2=df2.groupby('country')['people_vaccinated_per_hundred'].sum().reset_index(name ='Total_percent of people_vaccinated')
    #print(result2)
    Final_Result2=result2.sort_values(by='Total_percent of people_vaccinated', ascending=False)
    print(Final_Result2)


