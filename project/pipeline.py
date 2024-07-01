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

# Initial filtering of the data to include only valid countries and common years
co2_data_filtered = co2_data_cleaned[
    (co2_data_cleaned['country'].isin(valid_countries)) & 
    (co2_data_cleaned['year'].between(overall_common_start_year, overall_common_end_year))
]

energy_data_filtered = energy_data_cleaned[
    (energy_data_cleaned['country'].isin(valid_countries)) & 
    (energy_data_cleaned['year'].between(overall_common_start_year, overall_common_end_year))
]

print(f"Number of countries after initial filtering - CO2 Data: {co2_data_filtered['country'].nunique()}")
print(f"Number of countries after initial filtering - Energy Data: {energy_data_filtered['country'].nunique()}")

# Verify the filtering and remove countries with discrepancies
def verify_and_filter_years(data, start_year, end_year):
    year_range = data.groupby('country')['year'].agg(['min', 'max'])
    discrepancies = year_range[(year_range['min'] != start_year) | (year_range['max'] != end_year)]
    
    if not discrepancies.empty:
        print("There are discrepancies in the start and/or end years, removing these countries:")
        print(discrepancies)
        # Remove countries with discrepancies
        valid_countries = set(year_range[(year_range['min'] == start_year) & (year_range['max'] == end_year)].index)
        data = data[data['country'].isin(valid_countries)]
        print(f"Number of countries after removing discrepancies: {data['country'].nunique()}")
    else:
        print("All countries have the same start and end years.")
    
    return data

print("\nVerifying and Filtering CO2 Data Years:")
co2_data_filtered = verify_and_filter_years(co2_data_filtered, overall_common_start_year, overall_common_end_year)

print("\nVerifying and Filtering Energy Data Years:")
energy_data_filtered = verify_and_filter_years(energy_data_filtered, overall_common_start_year, overall_common_end_year)

# Adjust the final merge to include only countries present in both datasets
common_countries = set(co2_data_filtered['country']).intersection(set(energy_data_filtered['country']))

co2_data_filtered = co2_data_filtered[co2_data_filtered['country'].isin(common_countries)]
energy_data_filtered = energy_data_filtered[energy_data_filtered['country'].isin(common_countries)]

# Print final counts after ensuring common countries
print(f"Number of common countries in final filtered data - CO2 Data: {co2_data_filtered['country'].nunique()}")
print(f"Number of common countries in final filtered data - Energy Data: {energy_data_filtered['country'].nunique()}")

# Inspect column names to find the actual names for total energy production and CO2 emissions
print("\nCO2 Data Columns:")
print(co2_data_filtered.columns)

print("\nEnergy Data Columns:")
print(energy_data_filtered.columns)

# Merge datasets
merged_data = pd.merge(co2_data_filtered, energy_data_filtered, on=['country', 'year', 'iso_code'])

# Additional checks
print("\nChecking for duplicate rows...")
duplicates = merged_data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

print("\nChecking data types...")
print(merged_data.dtypes)

print("\nChecking for missing values in the merged data...")
missing_values = merged_data.isnull().sum()
print(missing_values)

print("\nSanity check on merged columns...")
expected_columns = [
    'country', 'year', 'iso_code', 'population_x', 'cement_co2', 'co2', 'co2_growth_abs', 
    'co2_growth_prct', 'co2_per_capita', 'coal_co2', 'coal_co2_per_capita', 'cumulative_co2', 
    'cumulative_coal_co2', 'cumulative_flaring_co2', 'cumulative_gas_co2', 'cumulative_luc_co2', 
    'cumulative_oil_co2', 'flaring_co2', 'flaring_co2_per_capita', 'gas_co2', 'gas_co2_per_capita', 
    'land_use_change_co2', 'land_use_change_co2_per_capita', 'oil_co2', 'oil_co2_per_capita', 
    'share_global_co2', 'share_global_coal_co2', 'share_global_cumulative_co2', 
    'share_global_cumulative_coal_co2', 'share_global_cumulative_luc_co2', 'share_global_luc_co2', 
    'share_of_temperature_change_from_ghg', 'temperature_change_from_ch4', 'temperature_change_from_co2', 
    'temperature_change_from_ghg', 'temperature_change_from_n2o', 'population_y', 'gdp', 
    'coal_prod_change_twh', 'coal_prod_per_capita', 'coal_production', 'energy_cons_change_pct', 
    'energy_cons_change_twh', 'gas_prod_change_twh', 'gas_prod_per_capita', 'gas_production', 
    'oil_prod_change_twh', 'oil_prod_per_capita', 'oil_production', 'primary_energy_consumption'
]
missing_columns = [col for col in expected_columns if col not in merged_data.columns]
extra_columns = [col for col in merged_data.columns if col not in expected_columns]

if not missing_columns and not extra_columns:
    print("All expected columns are present in the merged data.")
else:
    print(f"Missing columns: {missing_columns}")
    print(f"Extra columns: {extra_columns}")

# Function to store data in /data directory
def save_data(df, filename):
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    filepath = os.path.join(data_dir, filename)
    df.to_csv(filepath, index=False)

if __name__ == "__main__":
    # Save filtered datasets
    save_data(merged_data, 'merged_data.csv')
