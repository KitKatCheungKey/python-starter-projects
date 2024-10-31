import pandas as pd

filepath = 'adult.data.csv'

df = pd.DataFrame(pd.read_csv(filepath))

print(df.head())

males = df.loc[df['sex'] == 'Male']

malesmeanage = males['age'].mean()

df.info()

print(malesmeanage)

uniqueraces = df['race'].unique()

print(uniqueraces)

print('There are' ,df['race'].nunique() ,'races')

totalrecords = df.shape[0]
bachelordegree = df.loc[df['education'] == 'Bachelors'].shape[0]
nonbachelordegree = df.loc[df['education'] != 'Bachelors'].count
percentagebachelor = (bachelordegree / totalrecords) * 100


print(percentagebachelor)

#df = df[(df['col'] < -0.25) | (df['col'] > 0.25)]

advancededucation = df.loc[((df['education'] == 'Masters') | (df['education'] == 'Bachelors')| (df['education'] == 'Doctorate'))].shape[0]
advancededucationand50 = df.loc[((df['education'] == 'Masters') | (df['education'] == 'Bachelors')| (df['education'] == 'Doctorate')) &  (df['salary'] == '>50K')].shape[0]
percentageadvanced50 = (advancededucationand50/advancededucation) * 100

print(percentageadvanced50)

noadvancededucation50 = df.loc[((df['education'] != 'Masters') & (df['education'] != 'Bachelors') & (df['education'] != 'Doctorate') &  (df['salary'] == '>50K'))].shape[0]
noadvancededucationtotal = df.loc[((df['education'] != 'Masters') & (df['education'] != 'Bachelors') & (df['education'] != 'Doctorate'))].shape[0]
percentagenoadvanced50 = (noadvancededucation50 / noadvancededucationtotal) * 100

print(percentagenoadvanced50)

minhoursfullrow = df.nsmallest(1,'hours-per-week')
minhours = df['hours-per-week'].min()

print(minhours)

minhourstotal = df.loc[df['hours-per-week'] == df['hours-per-week'].min()].shape[0]
minhours50 = df.loc[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')].shape[0]

print((minhours50 / minhourstotal) * 100)

uniquecountires = df['native-country'].unique()

print(uniquecountires)

filteredcountries = df.loc[df['native-country'] != '?']
countrycounts = []
countrycounts2 = []


""" for countries in filteredcountries:
    #need another for loop here to iterate over the actual dataframe with all rows
    for records in df:
        if(df['native-country'] == countries):
            if(df['salary'] == '>50K'):
                countrycounts[countries] + 1
            else:
                countrycounts2[countries] + 1

            records = records + 1


countryover50 = []
    
for counts in filteredcountries:
    countryover50[counts] = (countrycounts[counts] / (countrycounts + countrycounts2)) * 100

print(countryover50.max()) """

#1. grab a list of all people who earn more than 50K
a = df['salary'] == '>50K'
#2. get the rest of the details for people who earn more than 50K
b = df[df['salary'] =='>50K']
#3. get just the native country field for the list of people who earn more than 50K
c = df[df['salary'] =='>50K']['native-country']
#4. Count the number of values of native country that appear in the list of people who earn more than 50K
d = df[df['salary'] =='>50K']['native-country'].value_counts()
#5. Find the number of rows each country has in the original dataframe
e = df['native-country'].value_counts()
#6. Divide the number counts of rows of people who earn more than 50K by  the row count per country in original dataframe * 100 for percentage
f = (df[df['salary'] =='>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100
#7. Sort the list descending so the highest percentage is at the top
e = ((df[df['salary'] =='>50K']['native-country'].value_counts() / df['native-country'].value_counts()) * 100).sort_values(ascending=False)


print(e)

highest_earning_country = e.index[0]
highest_earning_country_percentage = e[0]

print(highest_earning_country)
print(round(highest_earning_country_percentage,2))

india50k = df['native-country'] == 'India'
india50ka = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
india50kb = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
india50kc = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
india50kd = india50kc.index[0]

print(india50kd)







