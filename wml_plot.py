import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample data from the new dataset
data =  pd.read_csv('aggregated_data.csv')

# Create DataFrame
df = pd.DataFrame(data)

# Calculate hist_avg (for simplicity, using a constant value here; in practice, calculate based on full dataset)
hist_avg_values = {
    'OROVILLE/WML': df[df['topic'] == 'OROVILLE/WML']['TAF'].mean(),
    'SHASTA/WML': df[df['topic'] == 'SHASTA/WML']['TAF'].mean(),
    'SONOMA/WML': df[df['topic'] == 'SONOMA/WML']['TAF'].mean()
}

# Add hist_avg and capacity columns
df['hist_avg'] = df['topic'].map(hist_avg_values)
df['capacity'] = df['hist_avg'] * 2
df['storage'] = df['TAF']
df = df[df['Date'] == '10/7/2024']

# Plotting grouped bar chart
topics = df['topic']
bar_width = 0.25

# Set position of bars on X axis
r1 = np.arange(len(topics))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Create figure and axes
plt.figure(figsize=(12,6))

# Make the plot
bars1 = plt.bar(r1, df['hist_avg'], color='blue', width=bar_width, edgecolor='grey', label='hist_avg')
bars2 = plt.bar(r2, df['capacity'], color='orange', width=bar_width, edgecolor='grey', label='capacity')
bars3 = plt.bar(r3, df['storage'], color='green', width=bar_width, edgecolor='grey', label='storage')

# Add labels and title
plt.xlabel('Topics', fontweight='bold')
plt.ylabel('Values', fontweight='bold')
plt.xticks([r + bar_width for r in range(len(topics))], topics)
plt.title('Hist Avg, Capacity, and Storage by Topic for Date: October 1, 2024')

# Add legend
plt.legend()

# Add data callouts on top of the bars
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom')
for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom')
for bar in bars3:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, round(yval, 2), ha='center', va='bottom')

# Show plot
plt.show()