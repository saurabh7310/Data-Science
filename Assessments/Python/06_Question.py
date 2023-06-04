import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('pokemon_data.csv')

# Get all Pokemons whose spawn rate is less than 5%
spawn_rate_less_than_5 = df[df['Spawn Chance (%)'] < 5]
print("Pokemons with spawn rate less than 5%:")
print(spawn_rate_less_than_5[['Name', 'Spawn Chance (%)']])

# Get all Pokemons that have less than 4 weaknesses
less_than_4_weaknesses = df[df['Weaknesses'].str.split(',').apply(len) < 4]
print("Pokemons with less than 4 weaknesses:")
print(less_than_4_weaknesses[['Name', 'Weaknesses']])

# Get all Pokemons that have no multipliers at all
no_multipliers = df[df['multipliers'].isnull()]
print("Pokemons with no multipliers:")
print(no_multipliers[['Name', 'multipliers']])

# Get all Pokemons that do not have more than 2 evolutions
less_than_2_evolutions = df[df['Next Evolution'].str.split(',').apply(len) < 2]
print("Pokemons with less than 2 evolutions:")
print(less_than_2_evolutions[['Name', 'Next Evolution']])

# Get all Pokemons whose spawn time is less than 300 seconds
df['Spawn Time'] = pd.to_datetime(df['Spawn Time'], format='%M:%S')
spawn_time_less_than_300 = df[df['Spawn Time'].dt.total_seconds() < 300]
print("Pokemons with spawn time less than 300 seconds:")
print(spawn_time_less_than_300[['Name', 'Spawn Time']])

# Get all Pokemon who have more than two types of capabilities
more_than_2_types = df[df['Type'].str.split(',').apply(len) > 2]
print("Pokemons with more than 2 types of capabilities:")
print(more_than_2_types[['Name', 'Type']])

# Plotting the analysis

# Bar chart for Pokemons with less than 4 weaknesses
weakness_count = df['Weaknesses'].str.split(',').apply(len)
weakness_count.value_counts().sort_index().plot(kind='bar', color='blue')
plt.xlabel('Number of Weaknesses')
plt.ylabel('Count')
plt.title('Pokemons with Less Than 4 Weaknesses')
plt.show()

# Pie chart for the distribution of Pokemon types
type_counts = df['Type'].str.split(',').apply(len)
type_counts.value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.title('Distribution of Pokemon Types')
plt.show()
