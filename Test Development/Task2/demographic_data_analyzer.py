import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    uniqueraces = df['race'].unique()
    race_count = df['race'].value_counts()

    # What is the average age of men?
    males = df.loc[df['sex'] == 'Male']

    malesmeanage = males['age'].mean()

    average_age_men = round(malesmeanage,1)

    # What is the percentage of people who have a Bachelor's degree?
    totalrecords = df.shape[0]
    bachelordegree = df.loc[df['education'] == 'Bachelors'].shape[0]
    nonbachelordegree = df.loc[df['education'] != 'Bachelors'].count
    percentagebachelor = round(((bachelordegree / totalrecords) * 100),1)

    percentage_bachelors = percentagebachelor

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advancededucation = df.loc[((df['education'] == 'Masters') | (df['education'] == 'Bachelors')| (df['education'] == 'Doctorate'))].shape[0]
    advancededucationand50 = df.loc[((df['education'] == 'Masters') | (df['education'] == 'Bachelors')| (df['education'] == 'Doctorate')) &  (df['salary'] == '>50K')].shape[0]
    percentageadvanced50 = round(((advancededucationand50/advancededucation) * 100),1)

    noadvancededucation50 = df.loc[((df['education'] != 'Masters') & (df['education'] != 'Bachelors') & (df['education'] != 'Doctorate') &  (df['salary'] == '>50K'))].shape[0]
    noadvancededucationtotal = df.loc[((df['education'] != 'Masters') & (df['education'] != 'Bachelors') & (df['education'] != 'Doctorate'))].shape[0]
    percentagenoadvanced50 = round(((noadvancededucation50 / noadvancededucationtotal) * 100),1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = advancededucation
    lower_education = noadvancededucationtotal

    # percentage with salary >50K
    higher_education_rich = percentageadvanced50
    lower_education_rich = percentagenoadvanced50

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    minhoursfullrow = df.nsmallest(1,'hours-per-week')
    minhours = df['hours-per-week'].min()
    min_work_hours = minhours

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minhourstotal = df.loc[df['hours-per-week'] == df['hours-per-week'].min()].shape[0]
    minhours50 = df.loc[(df['hours-per-week'] == df['hours-per-week'].min()) & (df['salary'] == '>50K')].shape[0]

    num_min_workers = minhourstotal

    rich_percentage = round(((minhours50 / minhourstotal) * 100),1)

    # What country has the highest percentage of people that earn >50K?

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



    highest_earning_country = e.index[0]
    highest_earning_country_percentage = round(e[0],1)

    # Identify the most popular occupation for those who earn >50K in India.

    india50k = df['native-country'] == 'India'
    india50ka = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    india50kb = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation']
    india50kc = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts()
    india50kd = india50kc.index[0]

    top_IN_occupation = india50kd

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
