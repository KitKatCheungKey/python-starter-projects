import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

# 1

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd) 
print("Files in %r: %s" % (cwd, files))
df = pd.read_csv("medical_examination.csv")
print(df.head())

# 2
df['overweight'] = (df['weight']/((df['height'] /100) ** 2)) > 25 
df.replace({'overweight': {False : 0 , True : 1}},inplace = True)
print(df.head())

# 3
#df.loc[df['cholesterol'] == 1,'cholesterol'] = 0
#df.loc[df['cholesterol'] > 1 ,'cholesterol'] = 1
df['cholesterol'] = np.where(df['cholesterol'] == 1,0,1)
print(df)

#df.loc[df['gluc'] == 1,'gluc'] = 0
#df.loc[df['gluc'] > 1 ,'gluc'] = 1
df['gluc'] = np.where(df['gluc'] == 1,0,1)
print(df)


df_cat2 = df.iloc[:,[7,8, 9,10,11,12,13]]
df_cat2 = pd.melt(df_cat2)

print(df_cat2)


# 4
def draw_cat_plot():
   #5
   # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    #df_cat = df['cholesterol','gluc','smoke','alco','active','overweight']
    df_cat = pd.melt(df,id_vars = ['cardio'],value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])

    # 6 # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.

    

    # 7 # Draw the catplot with 'sns.catplot()'
    figure = sns.catplot(data = df_cat, x = 'variable', col = "cardio", kind = "count", hue =  "value").set_axis_labels('variable','total')
    

    # 8
    fig = figure.figure


    # 9
    fig.savefig('catplot.png')
    return fig

# https://www.geeksforgeeks.org/filter-pandas-dataframe-with-multiple-conditions/
# https://seaborn.pydata.org/generated/seaborn.catplot.html
# 10
#print('hi')
#df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] > df['height'].quantile(0.975)) & (df['weight'] < df['weight'].quantile(0.025)) & (df['weight'] > df['weight'].quantile(0.975))]
#df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
#print(df_heat.shape[0])
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))



    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(corr,mask=mask,square=True,annot = True,fmt= ".1f")


    # 16
    fig.savefig('heatmap.png')
    return fig