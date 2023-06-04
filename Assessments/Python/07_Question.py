import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('meteorite_landings.csv')

# Convert the year column to datetime
df['year'] = pd.to_datetime(df['year'], errors='coerce')

# Get all the Earth meteorites that fell before the year 2000
earth_meteorites_before_2000 = df[(df['reclat'].notnull()) & (df['year'].dt.year < 2000)]
print("Earth meteorites that fell before the year 2000:")
print(earth_meteorites_before_2000[['name', 'year']])

# Get all the Earth meteorites coordinates that fell before the year 1970
earth_meteorites_before_1970 = df[(df['reclat'].notnull()) & (df['year'].dt.year < 1970)]
print("Earth meteorites coordinates that fell before the year 1970:")
print(earth_meteorites_before_1970[['reclat', 'reclong']])

# Assuming that the mass of the earth meteorites was in kg, get all those whose mass was more than 10000 kg
earth_meteorites_mass_gt_10000 = df[(df['reclat'].notnull()) & (df['mass (g)'] > 10000)]
print("Earth meteorites with mass greater than 10000 kg:")
print(earth_meteorites_mass_gt_10000[['name', 'mass (g)']])

# Plotting the analysis

# Histogram of the year distribution for Earth meteorites
earth_meteorites_before_2000['year'].dt.year.hist(bins=30, color='blue')
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Distribution of Earth Meteorites before 2000')
plt.show()

# Scatter plot of the coordinates for Earth meteorites before 1970
plt.scatter(earth_meteorites_before_1970['reclong'], earth_meteorites_before_1970['reclat'], color='red')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Coordinates of Earth Meteorites before 1970')
plt.show()
