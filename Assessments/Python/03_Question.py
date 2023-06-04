import requests
import pandas as pd

def download_and_convert_to_excel(url, output_file):
    # Download the data from the provided link
    response = requests.get(url)
    data = response.json()

    # Convert the data to a structured format
    structured_data = []
    for item in data:
        structured_item = {
            'Name': item['name'],
            'Age': item['age'],
            'Email': item['email']
        }
        structured_data.append(structured_item)

    # Create a Pandas DataFrame from the structured data
    df = pd.DataFrame(structured_data)

    # Export the DataFrame to an Excel file
    df.to_excel(output_file, index=False)

    print(f"Data has been successfully converted and saved to '{output_file}'.")

# Example usage
url = "https://api.example.com/data"
output_file = "structured_data.xlsx"
download_and_convert_to_excel(url, output_file)
