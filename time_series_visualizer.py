import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv',index_col='date')

print(df.head())

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

print(df.head())

def draw_line_plot():
    # Draw line plot
    fig,axes = plt.subplots(figsize=(20,10))

    axes.plot(df.index.values,df['value'].values,data=df)
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axes.set_ylabel('Page Views')
    axes.set_xlabel('Date')

    #fig.set_label('Daily freeCodeCamp Forum Page Views ')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace= True)
    print(df_bar.columns)
    print(df_bar.head())
    df_bar['date'] = pd.to_datetime(df_bar['date'], format='%Y-%m-%d')
    #df_bar['month'] = None 
    df_bar['month'] = df_bar['date'].dt.month
    df_bar['year'] = df_bar['date'].dt.year


    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    df_bar['month'] = df_bar['month'].apply(lambda i: months[i-1])
    #this is to make sure that the months appear in order 
    df_bar['month'] = pd.Categorical(df_bar['month'],categories=months)
    print(df_bar.head())

    list_of_years = list(sorted(set(df_bar['year'])))

    print(list_of_years)


    #The error you're encountering, "TypeError: cannot unpack non-iterable Figure object," is due to a small mistake in your code when you're creating the figure and axes. 
    #In Matplotlib, the plt.subplots() function is commonly used to create a figure and one or more axes objects. 
    # However, in your code, you've used plt.figure() which only creates a figure object and doesn't return the axes.
    #fig = df_bar.pivot(index='date',columns='month',values='value').plot.bar()

    #EXAMPLE pivot_table_basic = df.pivot_table(
    #index='RepName', 
    #columns='Year',  
    #values=['Helpfulness', 'Courtesy', 'Empathy'],
    #aggfunc='mean'
    #)

    #fig = df_bar.plot(x='Year', kind = 'bar')
    
    # Draw bar plot

    df_bar2 = df_bar.pivot_table(index=['year'],columns='month',values='value',aggfunc='mean')

    print('this is df_bar2')
    print(df_bar2.head())
    print(df_bar2.info)

    axes = df_bar2.plot(kind='bar')
    

    #fig = plt.bar(df_bar.pivot(index='date',columns='month',values='value'),height=df_bar['value'])
    #axes.bar(x=['month'],height=['value'])
    #axes.bar(x=df_bar2['month','year'],height=df_bar2['value'],width = 0.5)
    #axes.bar(x=df_bar2['date'],height=df_bar2['value'],width=0.5)
    #axes.set_title('Average page views by month')
    axes.set_ylabel('Average Page Views')
    axes.set_xlabel('Years')
    #axes.set_xticks(df_bar['year'],list_of_years)

    fig = axes.get_figure()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    #had to change the provided code because it doesn't seem to work with my version of python 
    df_box['date'] = pd.to_datetime(df_box['date'], format='%Y-%m-%d')
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.month

    # Draw box plots (using Seaborn)

    #stacking two subplots next to each  other
    #fig, ax =plt.subplots(1,2)
    #sns.countplot(df['batting'], ax=ax[0])
    #sns.countplot(df['bowling'], ax=ax[1])


    #plot_objects = plt.subplots(nrows = 1,ncols = 2, figsize=(24,12))
    fig, ax = plt.subplots(1,2,figsize=(24,12))
    

    box1 = sns.boxplot(data=df_box, x='year',y='value',ax=ax[0])
    box1.set_title('Year-wise Box Plot (Trend)')
    box1.set_ylabel('Page Views')
    box1.set_xlabel('Year')
    box2 = sns.boxplot(data=df_box, x='month',y='value',ax=ax[1])
    box2.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    box2.set_ylabel('Page Views')
    box2.set_title('Month-wise Box Plot (Seasonality)')
    box2.set_xlabel('Month')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
