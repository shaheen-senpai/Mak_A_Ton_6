import pandas as pd
import matplotlib.pyplot as plt
fig,ax = plt.subplots(1,1,figsize=(12,10))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False) 
df=pd.read_csv("data.csv")
# Filter the dataframe for the desired columns
df_year = df['Year']

# Count the number of occurrences for each year
year_counts = df_year.value_counts()

# Generate a pie chart of the year counts
ax.pie(year_counts, labels=year_counts.index, autopct='%1.1f%%')

# Add title and labels
ax.set_title("Distribution of Years")
ax.set_xlabel("Year")

# Remove empty figure supertitle
fig.suptitle("")

# Adjust layout
fig.tight_layout()

# Save the figure as a PNG file
plt.savefig("year_pie_chart.png")
my_plot = plt.gcf()
my_plot.savefig('my_plot1.png')
