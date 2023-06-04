import requests
import csv

def download_and_convert_to_csv(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Extract the keys from the first item to use as column headers
    headers = list(data[0].keys())

    # Open the CSV file in write mode
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)

        # Write the column headers
        writer.writeheader()

        # Write each data item as a row in the CSV file
        writer.writerows(data)

    print(f"Data has been successfully converted and saved to '{output_file}'.")

# Example usage
url = "https://data.nasa.gov/resource/y77d-th95.json"
output_file = "nasa_data.csv"
download_and_convert_to_csv(url, output_file)
