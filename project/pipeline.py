import pandas as pd
import os

# Define URLs for datasets
co2_url = 'https://github.com/owid/co2-data/blob/master/owid-co2-data.csv?raw=true'
energy_url = 'https://github.com/owid/energy-data/blob/master/owid-energy-data.csv?raw=true'

# Load the data
co2_data = pd.read_csv(co2_url)
energy_data = pd.read_csv(energy_url)

# Display initial missing data percentages
print("Initial CO2 Data Missing Values (%):")
print((co2_data.isnull().mean() * 100).sort_values(ascending=False))
print("\nInitial Energy Data Missing Values (%):")
print((energy_data.isnull().mean() * 100).sort_values(ascending=False))

print("Initial CO2 Data Missing Values (%):")
print((co2_data.isnull().mean().mean() * 100))
print("\nInitial Energy Data Missing Values (%):")
print((energy_data.isnull().mean().mean() * 100))

# Drop columns with more than 50% missing values
co2_data_cleaned = co2_data.dropna(thresh=0.5 * len(co2_data), axis=1)
energy_data_cleaned = energy_data.dropna(thresh=0.5 * len(energy_data), axis=1)

# Drop rows with any remaining missing values
co2_data_cleaned = co2_data_cleaned.dropna()
energy_data_cleaned = energy_data_cleaned.dropna()

# Display missing data percentages after dropping rows
print("\nCO2 Data Missing Values After Dropping Rows (%):")
print((co2_data_cleaned.isnull().mean() * 100).sort_values(ascending=False))
print("\nEnergy Data Missing Values After Dropping Rows (%):")
print((energy_data_cleaned.isnull().mean() * 100).sort_values(ascending=False))

print("\nCO2 Data Missing Values After Dropping Rows (%):")
print((co2_data_cleaned.isnull().mean().mean() * 100))
print("\nEnergy Data Missing Values After Dropping Rows (%):")
print((energy_data_cleaned.isnull().mean().mean() * 100))

# Identify the common year range across all countries
common_years_co2 = co2_data_cleaned.groupby('country')['year'].agg(['min', 'max']).reset_index()
common_years_energy = energy_data_cleaned.groupby('country')['year'].agg(['min', 'max']).reset_index()

# Merge to find common start and end years
common_years = common_years_co2.merge(common_years_energy, on='country', suffixes=('_co2', '_energy'))
common_years['common_start_year'] = common_years[['min_co2', 'min_energy']].max(axis=1)
common_years['common_end_year'] = common_years[['max_co2', 'max_energy']].min(axis=1)

# Filter out countries with no overlapping years
common_years = common_years[common_years['common_start_year'] <= common_years['common_end_year']]

# Create a set of countries with valid year ranges
valid_countries = set(common_years['country'])

# Determine overall common start and end years
overall_common_start_year = common_years['common_start_year'].max()
overall_common_end_year = common_years['common_end_year'].min()

print(f"Overall Common Start Year: {overall_common_start_year}")
print(f"Overall Common End Year: {overall_common_end_year}")

# Filter the data to include only valid countries and common years
co2_data_filtered = co2_data_cleaned[
    (co2_data_cleaned['country'].isin(valid_countries)) & 
    (co2_data_cleaned['year'].between(overall_common_start_year, overall_common_end_year))
]

energy_data_filtered = energy_data_cleaned[
    (energy_data_cleaned['country'].isin(valid_countries)) & 
    (energy_data_cleaned['year'].between(overall_common_start_year, overall_common_end_year))
]

# Verify the filtering
def verify_years(data, start_year, end_year):
    year_range = data.groupby('country')['year'].agg(['min', 'max'])
    if all(year_range['min'] == start_year) and all(year_range['max'] == end_year):
        print("All countries have the same start and end years.")
    else:
        print("There are discrepancies in the start and/or end years:")
        print(year_range[year_range['min'] != start_year])
        print(year_range[year_range['max'] != end_year])

print("\nVerifying CO2 Data Years:")
verify_years(co2_data_filtered, overall_common_start_year, overall_common_end_year)

print("\nVerifying Energy Data Years:")
verify_years(energy_data_filtered, overall_common_start_year, overall_common_end_year)

# Merge datasets
merged_data = pd.merge(co2_data_filtered, energy_data_filtered, on=['country', 'year', 'iso_code'])

# Function to store data in /data directory
def save_data(df, filename):
    # Use the absolute path to the data directory
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    filepath = os.path.join(data_dir, filename)
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    
    # Save filtered datasets
    save_data(merged_data, 'merged_data.csv')
