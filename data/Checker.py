import pandas as pd

# Load the merged data
merged_data = pd.read_csv('merged_data.csv')

# Check the unique countries and their year range to confirm consistency
unique_countries = merged_data['country'].unique()
print(f"Unique countries in the merged data: {len(unique_countries)}")

# Verify the year range
year_range = merged_data.groupby('country')['year'].agg(['min', 'max'])
print(year_range)

# Determine the common start and end years based on the merged data
common_start_year = year_range['min'].max()
common_end_year = year_range['max'].min()

# Ensure there are no discrepancies
if all(year_range['min'] == common_start_year) and all(year_range['max'] == common_end_year):
    print("All countries have the same start and end years in the merged data.")
else:
    print("There are still discrepancies in the merged data:")
    print(year_range[(year_range['min'] != common_start_year) | (year_range['max'] != common_end_year)])

# Check for duplicate rows
print("\nChecking for duplicate rows...")
duplicates = merged_data.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Check data types
print("\nChecking data types...")
print(merged_data.dtypes)

# Check for missing values
print("\nChecking for missing values in the merged data...")
missing_values = merged_data.isnull().sum()
print(missing_values)

# Simplified sanity check on key columns
key_columns = ['country', 'year', 'co2', 'primary_energy_consumption']
missing_columns = [col for col in key_columns if col not in merged_data.columns]

if not missing_columns:
    print("All key columns are present in the merged data.")
else:
    print(f"Missing key columns: {missing_columns}")

# Verify the structure of the merged data
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
