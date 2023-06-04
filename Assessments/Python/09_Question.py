import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
url = 'https://data.wa.gov/api/views/f6w7-q2d2/rows.csv?accessType=DOWNLOAD'
df = pd.read_csv(url)

# Get all the cars and their types that do not qualify for clean alternative fuel vehicle
not_qualify_cafv = df[df['Clean Alternative Fuel Vehicle (CAFV) Eligibility'] == 'No']
not_qualify_cafv_cars = not_qualify_cafv[['Vehicle Make', 'Vehicle Type']]
print("Cars and their types that do not qualify for clean alternative fuel vehicle:")
print(not_qualify_cafv_cars)

# Get all TESLA cars with the model year, and model type made in Bothell City
tesla_cars_bothell = df[(df['Vehicle Make'] == 'TESLA') & (df['City'] == 'BOTHELL')]
tesla_cars_info = tesla_cars_bothell[['Model Year', 'Model Type']]
print("TESLA cars with model year and model type made in Bothell City:")
print(tesla_cars_info)

# Get all the cars that have an electric range of more than 100 and were made after 2015
cars_electric_range_gt_100 = df[(df['Electric Range'] > 100) & (df['Model Year'] > 2015)]
print("Cars with electric range more than 100 and made after 2015:")
print(cars_electric_range_gt_100)

# Draw plots to show the distribution between city and electric vehicle type
plt.figure(figsize=(12, 6))
city_ev_type_distribution = df.groupby(['City', 'Electric Vehicle Type']).size().unstack()
city_ev_type_distribution.plot(kind='bar', stacked=True)
plt.xlabel('City')
plt.ylabel('Count')
plt.title('Distribution of Electric Vehicle Types by City')
plt.legend(loc='upper right')
plt.show()
