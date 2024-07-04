import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os

# Load the merged data
merged_data = pd.read_csv('merged_data.csv')

# List of selected countries
selected_countries = [
    'United States', 'China', 'India', 'Brazil', 
    'Germany', 'Russia', 'Japan', 'South Africa', 
    'Australia', 'Canada'
]

# Filter data for selected countries
filtered_data = merged_data[merged_data['country'].isin(selected_countries)]

# Initialize a dictionary to store results
country_results = {}

# Ensure the directory exists
output_dir = 'country_analysis'
os.makedirs(output_dir, exist_ok=True)

# Perform regression analysis for each country
for country in selected_countries:
    country_data = filtered_data[filtered_data['country'] == country]
    X = country_data['primary_energy_consumption']
    y = country_data['co2']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    country_results[country] = model.summary()

    # Plotting the results for visualization
    plt.figure()
    plt.scatter(X['primary_energy_consumption'], y, label='Data Points')
    plt.plot(X['primary_energy_consumption'], model.predict(X), color='red', label='Regression Line')
    plt.xlabel('Primary Energy Consumption')
    plt.ylabel('CO2 Emissions')
    plt.title(f'CO2 Emissions vs. Energy Production in {country}')
    plt.legend()
    plt.savefig(f'{output_dir}/{country}_regression.png')
    plt.show()

# Print summary for each country
for country, summary in country_results.items():
    print(f"\n{country} Regression Summary:\n{summary}\n")
