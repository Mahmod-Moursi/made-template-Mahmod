import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load the merged data
merged_data = pd.read_csv('merged_data.csv')

# List of countries for analysis
countries = ["United States", "China", "India", "Brazil", "Germany", "Russia", "Japan", "South Africa", "Australia", "Canada"]

# Initialize lists to store comparative metrics
coef_energy_list = []
coef_gdp_list = []
r_squared_list = []

# Print key statistics for each country
for country in countries:
    country_data = merged_data[merged_data['country'] == country]
    
    # Time series analysis
    print(f"{country} Time Series Analysis:")
    print(country_data[['year', 'co2', 'primary_energy_consumption']])
    
    # Regression analysis
    X = country_data[['primary_energy_consumption', 'gdp']]
    y = country_data['co2']
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    summary = model.summary()
    
    # Extract key statistics
    r_squared = model.rsquared
    coef_energy = model.params['primary_energy_consumption']
    coef_gdp = model.params['gdp']
    
    print(f"\n{country} Regression Summary:")
    print(f"R-squared: {r_squared}")
    print(f"Coefficient for energy consumption: {coef_energy}")
    print(f"Coefficient for GDP: {coef_gdp}")
    print(summary)
    print("\n")
    
    # Store comparative metrics
    coef_energy_list.append(coef_energy)
    coef_gdp_list.append(coef_gdp)
    r_squared_list.append(r_squared)

# Print comparative metrics
print("Comparative Metrics:")
print("Coefficients for Energy Consumption:", coef_energy_list)
print("Coefficients for GDP:", coef_gdp_list)
print("R-squared values:", r_squared_list)

# Create comparative charts (bar charts)
fig, axes = plt.subplots(3, 1, figsize=(10, 15))

# Coefficients for Energy Consumption
axes[0].bar(countries, coef_energy_list)
axes[0].set_title('Coefficient of Energy Consumption Comparison')
axes[0].set_ylabel('Coefficient')
axes[0].set_xticklabels(countries, rotation=45, ha='right')

# Coefficients for GDP
axes[1].bar(countries, coef_gdp_list)
axes[1].set_title('Coefficient of GDP Comparison')
axes[1].set_ylabel('Coefficient')
axes[1].set_xticklabels(countries, rotation=45, ha='right')

# R-squared values
axes[2].bar(countries, r_squared_list)
axes[2].set_title('R-squared Values Comparison')
axes[2].set_ylabel('R-squared')
axes[2].set_xticklabels(countries, rotation=45, ha='right')

plt.tight_layout()
plt.show()
