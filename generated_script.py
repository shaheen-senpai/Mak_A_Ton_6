import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots(1,1,figsize=(12,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False) 
df=pd.read_csv("data.csv")
# Filter columns
age_data = df['Age']
# Count frequency of each age
age_counts = age_data.value_counts()
# Plot pie chart
ax.pie(age_counts, labels=age_counts.index, autopct='%1.1f%%')
# Set title and axes labels
ax.set_title("Distribution of Age")
ax.set_xlabel("Age")
ax.set_ylabel("Percentage")
my_plot = plt.gcf()
my_plot.savefig('my_plot1.png')
