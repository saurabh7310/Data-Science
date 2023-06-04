import requests
import json

def download_and_extract_data(url):
    # Download the data from the provided API link
    response = requests.get(url)
    data = response.json()

    # Extract the show name and premiered date
    show_name = data['name']
    premiered_date = data['premiered']

    # Extract the episode data
    episode_data = data['_embedded']['episodes']
    episodes = []

    for episode in episode_data:
        episode_number = episode['number']
        episode_name = episode['name']
        episode_season = episode['season']
        episode_summary = episode['summary']

        # Remove HTML tags from the episode summary
        episode_summary = episode_summary.replace("<p>", "").replace("</p>", "")

        episode_info = {
            'Episode Number': episode_number,
            'Episode Name': episode_name,
            'Season': episode_season,
            'Summary': episode_summary
        }

        episodes.append(episode_info)

    # Print the extracted data
    print("Show Name:", show_name)
    print("Premiered Date:", premiered_date)
    print("\nEpisodes:")
    for episode in episodes:
        print(f"Episode {episode['Episode Number']}")
        print(f"Name: {episode['Episode Name']}")
        print(f"Season: {episode['Season']}")
        print(f"Summary: {episode['Summary']}")
        print()

# Example usage
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
download_and_extract_data(url)
