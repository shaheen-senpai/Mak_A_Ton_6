import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
fig,ax = plt.subplots(1,1,figsize=(12,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False) 
df=pd.read_csv("data.csv")
# Create a pie chart for age
age_counts = df['Age'].value_counts()
labels = age_counts.index
values = age_counts.values

ax.pie(values, labels=labels, startangle=90, autopct='%1.1f%%')
ax.axis('equal')

plt.title('Distribution of Age')
plt.xlabel('Age')
my_plot = plt.gcf()
my_plot.savefig('my_plot1.png')
