import requests
import pandas as pd

def download_and_convert_to_excel(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Extract the required attributes from each Pokemon entry
    structured_data = []
    for pokemon in data['pokemon']:
        attributes = {
            'ID': pokemon['id'],
            'Number': pokemon['num'],
            'Name': pokemon['name'],
            'Image URL': pokemon['img'],
            'Type': ', '.join(pokemon['type']),
            'Height': pokemon['height'],
            'Weight': pokemon['weight'],
            'Candy': pokemon.get('candy', ''),
            'Candy Count': pokemon.get('candy_count', ''),
            'Egg Distance (km)': pokemon.get('egg', ''),
            'Spawn Chance (%)': pokemon.get('spawn_chance', ''),
            'Avg Spawns': pokemon.get('avg_spawns', ''),
            'Spawn Time': pokemon.get('spawn_time', ''),
            'Weaknesses': ', '.join(pokemon.get('weaknesses', [])),
            'Next Evolution': ', '.join([
                f"{evolution['num']}: {evolution['name']}"
                for evolution in pokemon.get('next_evolution', [])
            ]),
            'Previous Evolution': ', '.join([
                f"{evolution['num']}: {evolution['name']}"
                for evolution in pokemon.get('prev_evolution', [])
            ])
        }
        structured_data.append(attributes)

    # Create a Pandas DataFrame from the structured data
    df = pd.DataFrame(structured_data)

    # Export the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

    print(f"Data has been successfully converted and saved to '{output_file}'.")

# Example usage
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
output_file = "pokemon_data.xlsx"
download_and_convert_to_excel(url, output_file)
