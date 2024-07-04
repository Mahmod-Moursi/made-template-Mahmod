import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load the merged data
merged_data = pd.read_csv('merged_data.csv')

# Display the shape of the dataset
print(f"The dataset contains {merged_data.shape[0]} rows and {merged_data.shape[1]} columns.")

# # Display the first few rows of the dataset
# print(merged_data.head())

# Display basic statistics of the dataset
# print(merged_data.describe())

# Check for missing values
missing_values = merged_data.isnull().sum()
print("Missing values in each column:")
print(missing_values[missing_values > 0])

# # Check data types
# print(merged_data.dtypes)

# # Histograms for numerical columns
numerical_columns = merged_data.select_dtypes(include=['float64', 'int64']).columns
num_cols = len(numerical_columns)
num_rows = (num_cols // 4) + 1  # Adjust number of rows based on the number of columns

# fig, axes = plt.subplots(nrows=num_rows, ncols=4, figsize=(20, 5*num_rows))
# axes = axes.flatten()

# for i, col in enumerate(numerical_columns):
#     merged_data[col].hist(bins=15, ax=axes[i])
#     axes[i].set_title(col)
#     axes[i].set_xlabel('Value')
#     axes[i].set_ylabel('Frequency')

# plt.tight_layout()
# plt.show()

# # Scatter plot of CO2 emissions vs. energy production
# plt.figure(figsize=(10, 6))
# sns.scatterplot(x='primary_energy_consumption', y='co2', data=merged_data)
# plt.xlabel('Total Energy Production')
# plt.ylabel('Total CO2 Emissions')
# plt.title('CO2 Emissions vs. Energy Production (2007-2016)')
# plt.show()

# # Correlation matrix (only numerical columns)
# numerical_columns = merged_data.select_dtypes(include=['float64', 'int64']).columns
# correlation_matrix = merged_data[numerical_columns].corr()
# plt.figure(figsize=(12, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Correlation Matrix')
# plt.show()
# # Check the numerical columns included in the heatmap
# print(numerical_columns)

# # Focused Heatmap
# key_columns = ['co2', 'primary_energy_consumption', 'gdp', 'coal_co2', 'oil_co2', 'gas_co2', 'population_x', 'energy_cons_change_twh', 'energy_cons_change_pct', 'temperature_change_from_co2']
# focused_correlation_matrix = merged_data[key_columns].corr()
# plt.figure(figsize=(10, 6))
# sns.heatmap(focused_correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
# plt.title('Focused Correlation Matrix')
# # plt.savefig('/mnt/data/focused_correlation_matrix.png')
# plt.show()


# # Line plot of CO2 emissions and energy production over time for a specific country
# country = 'United States'
# country_data = merged_data[merged_data['country'] == country]

# plt.figure(figsize=(10, 6))
# plt.plot(country_data['year'], country_data['co2'], label='CO2 Emissions')
# plt.plot(country_data['year'], country_data['primary_energy_consumption'], label='Energy Production')
# plt.xlabel('Year')
# plt.ylabel('Values')
# plt.title(f'CO2 Emissions and Energy Production Over Time in {country}')
# plt.legend()
# plt.show()

# # Box plots for numerical columns to identify outliers
# plt.figure(figsize=(15, 10))
# merged_data[numerical_columns].boxplot()
# plt.xticks(rotation=90)
# plt.title('Box plots of numerical columns')
# plt.show()

# # Calculate and display correlation
# correlation = merged_data['primary_energy_consumption'].corr(merged_data['co2'])
# print(f"Correlation between energy production and CO2 emissions: {correlation}")

# # Linear regression analysis
# X = merged_data['primary_energy_consumption']
# y = merged_data['co2']
# X = sm.add_constant(X)
# model = sm.OLS(y, X).fit()
# print(model.summary())

# # Residual plot
# residuals = model.resid
# plt.figure(figsize=(10, 6))
# sns.histplot(residuals, kde=True)
# plt.title('Distribution of Residuals')
# plt.xlabel('Residuals')
# plt.ylabel('Frequency')
# plt.show()

# # Plot residuals vs. fitted values
# fitted_values = model.fittedvalues
# plt.figure(figsize=(10, 6))
# plt.scatter(fitted_values, residuals)
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Residuals vs. Fitted Values')
# plt.xlabel('Fitted Values')
# plt.ylabel('Residuals')
# plt.show()

# Calculate VIF for each numerical column
X = merged_data[numerical_columns].dropna()
vif = pd.DataFrame()
vif['Variable'] = X.columns
vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)
