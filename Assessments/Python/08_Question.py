import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('tv_episodes_ratings.csv')

# Convert the air date column to datetime
df['airdate'] = pd.to_datetime(df['airdate'], errors='coerce')

# Get all the overall ratings for each season
season_ratings = df.groupby('season')['rating'].mean().sort_index()
print("Overall ratings for each season:")
print(season_ratings)

# Plotting the ratings for each season
season_ratings.plot(kind='bar', color='blue')
plt.xlabel('Season')
plt.ylabel('Average Rating')
plt.title('Average Ratings for Each Season')
plt.show()

# Get all the episode names whose average rating is more than 8 for every season
high_rated_episodes = df.groupby(['season', 'name'])['rating'].mean().unstack()
high_rated_episodes = high_rated_episodes[high_rated_episodes > 8].stack().reset_index(level=1, drop=True)
print("Episode names with average rating more than 8 for every season:")
print(high_rated_episodes)

# Get all the episode names that aired before May 2019
episodes_before_2019 = df[df['airdate'].dt.year < 2019]
episodes_before_2019 = episodes_before_2019[episodes_before_2019['airdate'].dt.month < 5]
print("Episode names that aired before May 2019:")
print(episodes_before_2019['name'])

# Get the episode name from each season with the highest and lowest rating
highest_rated_episodes = df.groupby('season')['rating'].idxmax()
lowest_rated_episodes = df.groupby('season')['rating'].idxmin()
highest_rated_episode_names = df.loc[highest_rated_episodes, ['season', 'name']]
lowest_rated_episode_names = df.loc[lowest_rated_episodes, ['season', 'name']]
print("Episode names with highest rating in each season:")
print(highest_rated_episode_names)
print("Episode names with lowest rating in each season:")
print(lowest_rated_episode_names)

# Get the summary for the most popular (highest rated) episode in every season
most_popular_episodes = df.groupby('season')['rating'].idxmax()
most_popular_episode_summary = df.loc[most_popular_episodes, ['season', 'name', 'summary']]
print("Summary for the most popular episode in each season:")
print(most_popular_episode_summary)
