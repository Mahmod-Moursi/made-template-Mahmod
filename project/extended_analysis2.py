import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

# Load the dataset
data = pd.read_csv('merged_data.csv')

# List of countries for analysis
countries = ["United States", "China", "India", "Brazil", "Germany", "Russia", "Japan", "South Africa", "Australia", "Canada"]

# Create output directory
output_dir = 'country_analysis_output'
os.makedirs(output_dir, exist_ok=True)

# Time Series Analysis
for country in countries:
    country_data = data[data['country'] == country]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['year'], country_data['primary_energy_consumption'], label='Energy Consumption')
    plt.plot(country_data['year'], country_data['co2'], label='CO2 Emissions')
    plt.xlabel('Year')
    plt.ylabel('Values')
    plt.title(f'Energy Consumption and CO2 Emissions Over Time in {country}')
    plt.legend()
    plt.savefig(os.path.join(output_dir, f'{country}_time_series.png'))
    plt.close()

# Density Plots
for country in countries:
    country_data = data[data['country'] == country]
    plt.figure(figsize=(10, 6))
    sns.kdeplot(country_data['primary_energy_consumption'], label='Energy Consumption', fill=True)
    sns.kdeplot(country_data['co2'], label='CO2 Emissions', fill=True)
    plt.xlabel('Values')
    plt.ylabel('Density')
    plt.title(f'Density Plot of Energy Consumption and CO2 Emissions in {country}')
    plt.legend()
    plt.savefig(os.path.join(output_dir, f'{country}_density_plot.png'))
    plt.close()

# Comparative Analysis with Bar Charts
regression_results = []

for country in countries:
    country_data = data[data['country'] == country]
    X = country_data[['primary_energy_consumption', 'gdp']]  # Add GDP to the model
    y = country_data['co2']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    regression_results.append({
        'country': country,
        'coefficient_energy': model.params['primary_energy_consumption'],
        'coefficient_gdp': model.params['gdp'],
        'r_squared': model.rsquared
    })

results_df = pd.DataFrame(regression_results)

# Bar Chart for Energy Consumption Coefficient
plt.figure(figsize=(12, 8))
sns.barplot(x='country', y='coefficient_energy', data=results_df)
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('Coefficient for Energy Consumption')
plt.title('Coefficient for Energy Consumption by Country')
plt.savefig(os.path.join(output_dir, 'coefficient_energy_comparison.png'))
plt.close()

# Bar Chart for GDP Coefficient
plt.figure(figsize=(12, 8))
sns.barplot(x='country', y='coefficient_gdp', data=results_df)
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('Coefficient for GDP')
plt.title('Coefficient for GDP by Country')
plt.savefig(os.path.join(output_dir, 'coefficient_gdp_comparison.png'))
plt.close()

# Bar Chart for R-squared values
plt.figure(figsize=(12, 8))
sns.barplot(x='country', y='r_squared', data=results_df)
plt.xticks(rotation=45)
plt.xlabel('Country')
plt.ylabel('R-squared Value')
plt.title('R-squared Value by Country')
plt.savefig(os.path.join(output_dir, 'r_squared_comparison.png'))
plt.close()

print("Extended analysis completed and results saved.")
