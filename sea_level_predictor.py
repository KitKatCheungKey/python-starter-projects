import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    print(df.head())

    # Create scatter plot

    
    print(df.info())
    print(df['Year'].size)
    print(df['CSIRO Adjusted Sea Level'].size)
    plt.scatter(data= df, x= 'Year',y='CSIRO Adjusted Sea Level')

    # Create first line of best fit

    #assign x and y values to find the slope and intercept using linregress
    x =  df['Year']
    y = df['CSIRO Adjusted Sea Level']

    slope, intercept, r_value, p_value, std_err = linregress(x, y) 

    #find y values , y = mx + c
    #if we were to just plot the values in the same scatter graph then this is all that is needed
    #y2 = [slope*xp + intercept for xp in x]
    #plt.plot(x,y2)

    #But since we need to project the line  to predict what happens in 2050 then we just take the same slope m and intercept c to compute using a new set of x in y=mx+c
    #The new set of x will be in the range of 1880 to 2050, since we want the line to go through 2050 we make a list of years from 1880 to 2051 in increments of 1 year
    moreyears = list(range(1880,2051,1))
    #plt.axline(xy1=(intercept,0),slope = slope)
    #find the y values for the new set of x described by moreyears
    extendedline = [slope * my + intercept for my in moreyears]
    #plot the line with the new years as x and the calculated values as y
    plt.plot(moreyears, extendedline)

    #plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    #plt.xlim(1850,2075)
    #plt.ylim(0,16)

    
    

    # Create second line of best fit

    df2000 = df.copy()
    df2000.reset_index(inplace=True)
    df2000 = df2000[df2000['Year'] >= 2000]

    print('this is df2000')
    print(df2000.head())

    x3 = df2000['Year']
    y3 = df2000['CSIRO Adjusted Sea Level']

    x3.reset_index
    y3.reset_index

    print(x3.head())
    print(y3.head())

    slope2, intercept2,r_value2,p_value2, std_err2 = linregress(x3,y3)

    #same as above, but we make an extended line for the new calculated slope and project it until 2051 so it can go through 2050
    moreyears2 = list(range(2000,2051,1))

    y4 = [slope2 * xi + intercept2 for xi in moreyears2]

    print(y4.count)

    plt.plot(moreyears2,y4)
    #plt.axline(xy1= [intercept2,0],slope=slope2)

    # Add labels and title
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()