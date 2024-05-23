import pandas as pd
import os

# Define URLs for datasets
co2_data_url = "https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv"
# Update with the actual URL for the temperature anomalies dataset when available
temperature_data_url = "https://example.com/temperature-anomalies.csv"

# Define selected countries and years range
selected_countries = ['United States', 'China', 'India', 'Brazil', 'Germany', 'Russia', 'Japan', 'South Africa', 'Australia', 'Canada']
#based on the common years from the temperature anomalies file, will be changed once the temperature anomalies file is provided.
start_year = 1850
end_year = 2022

# Function to load and filter CO2 dataset
def load_and_filter_co2_data(url):
    co2_df = pd.read_csv(url)
    co2_df = co2_df[co2_df['country'].isin(selected_countries)]
    co2_df = co2_df[(co2_df['year'] >= start_year) & (co2_df['year'] <= end_year)]
    co2_df = co2_df[['country', 'year', 'total_ghg']]  # Select required columns
    co2_df = co2_df.dropna(subset=['total_ghg'])  # Remove rows with missing total_ghg values
    return co2_df

# Function to load and filter temperature anomalies dataset
def load_and_filter_temperature_data(url):
    # Placeholder function until actual dataset URL is available
    pass

# Function to store data in /data directory
def save_data(df, filename):
    # Use the absolute path to the data directory
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    filepath = os.path.join(data_dir, filename)
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    # Load and filter CO2 dataset
    co2_df = load_and_filter_co2_data(co2_data_url)

    # Load and filter temperature anomalies dataset (placeholder until actual URL available)
    # temperature_df = load_and_filter_temperature_data(temperature_data_url)

    # Save filtered datasets
    save_data(co2_df, 'co2_data_filtered.csv')
    # save_data(temperature_df, 'temperature_data_filtered.csv')
