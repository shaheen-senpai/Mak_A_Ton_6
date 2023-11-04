import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots(1,1,figsize=(12,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False) 
df=pd.read_csv("data.csv")
df['flag'] = df['flag'].astype('category')
fig,ax = plt.subplots(1,1,figsize=(12,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
colors = {'F':'red', 'R':'green', 'P':'blue'}
ax.scatter(df.index, df['flag'], c=df['flag'].map(colors))
ax.set_xlabel('Index')
ax.set_ylabel('Flag')
ax.set_title('Scatter Plot of Flag')
my_plot = plt.gcf()
my_plot.savefig('my_plot1.png')
