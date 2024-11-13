import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Define the file path
file_path = r'C:\Users\sukie\OneDrive\Desktop\AI\PANDAS AND SEABORN\tips.csv'

# Extract the file name from the path
file_name = os.path.basename(file_path)

# Load the dataset
tips = pd.read_csv(file_path)

# Display the name of the dataset dynamically
print(f"Dataset name: {file_name}")
print(tips.head())  # Display the first few rows

print("\n")
print("Exercise 3:")
# Create a pandas DataFrame from the loaded dataset
df = pd.DataFrame(tips)

# Display the DataFrame
print(df)
print("\n")
print("Exercise 4:")
# Create a scatter plot showing the bill amount on the x axis and the tip amount on the y axis
sns.scatterplot(data=df, x='total_bill', y='tip')

# Display the plot
plt.show()

print("\n")
print("Exercise 5:")

# Set the seaborn style and font scale
sns.set(style="darkgrid", font_scale=1.2)

# Create a scatter plot showing the bill amount on the x axis and the tip amount on the y axis with the new settings
sns.scatterplot(data=df, x='total_bill', y='tip')

# Display the plot
plt.show()

print("\n")
print("Exercise 6:")

# Create a scatter plot showing the bill amount on the x axis and the tip amount on the y axis
# Use the 'day' column to assign marker colors
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day')

# Display the plot
plt.show()

print("\n")
print("Exercise 7:")

# Create a scatter plot showing the bill amount on the x axis and the tip amount on the y axis
# Use the 'day' column to assign marker colors and 'size' column to assign marker sizes
sns.scatterplot(data=df, x='total_bill', y='tip', hue='day', size='size')

# Display the plot
plt.show()

print("\n")
print("Exercise 8:")

# Create two subplots, each displaying data for a different value of the 'time' column
g = sns.FacetGrid(df, col="time")
g.map(sns.scatterplot, "total_bill", "tip")

# Display the plots
plt.show()

print("\n")
print("Exercise 9:")

# Create a FacetGrid with subplots for each combination of 'time' and 'sex'
g = sns.FacetGrid(df, col="time", row="sex")
g.map(sns.scatterplot, "total_bill", "tip")

# Display the plots
plt.show()