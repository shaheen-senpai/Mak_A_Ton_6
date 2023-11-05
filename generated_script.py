import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots(1,1,figsize=(12,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False) 
df=pd.read_csv("data.csv")
# Filter the dataframe to only include the 'year' column
year_df = df['year']

# Group the values by year and count the occurrences
year_counts = year_df.value_counts()

# Get the labels and sizes for the pie chart
labels = year_counts.index.tolist()
sizes = year_counts.values.tolist()

# Create the pie chart
plt.pie(sizes, labels=labels, startangle=90, autopct='%1.1f%%')
plt.axis('equal')

# Set the title and labels
plt.title('Distribution of Years')
plt.xlabel('Year')

# Set the x and y axes labels
plt.xlabel('Year')
plt.ylabel('Percentage')

# Remove the figure suptitle
fig.suptitle('')

# Show the graph
my_plot = plt.gcf()
my_plot.savefig('my_plot1.png')
