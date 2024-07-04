import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load the merged data
merged_data = pd.read_csv('merged_data.csv')

# Select only numerical columns for correlation matrix
numerical_columns = merged_data.select_dtypes(include=['float64', 'int64']).columns
numerical_data = merged_data[numerical_columns]

# Calculate the correlation matrix
correlation_matrix = numerical_data.corr().abs()

# Identify pairs of highly correlated variables (correlation > 0.9)
high_corr_pairs = np.where(correlation_matrix > 0.9)
high_corr_pairs = [(correlation_matrix.columns[x], correlation_matrix.columns[y]) for x, y in zip(*high_corr_pairs) if x != y and x < y]

# Print highly correlated pairs
print("Highly correlated pairs:")
for pair in high_corr_pairs:
    print(pair)

# Remove one of each pair of highly correlated variables
to_remove = set()
for x, y in high_corr_pairs:
    to_remove.add(y)  # Remove the second variable in each pair

# Create a new dataframe with the selected columns
reduced_data = merged_data.drop(columns=list(to_remove))

# Verify that multicollinearity is reduced
def calculate_vif(df):
    vif = pd.DataFrame()
    vif["Variable"] = df.columns
    vif["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]
    return vif

# Select numerical columns for VIF calculation
numerical_columns_reduced = reduced_data.select_dtypes(include=['float64', 'int64']).columns
reduced_numerical_data = reduced_data[numerical_columns_reduced]

# Calculate VIF for the reduced set of variables
vif = calculate_vif(reduced_numerical_data.dropna())
print(vif)

# Standardize the data before applying PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(reduced_numerical_data.dropna())

# Apply PCA
pca = PCA()
principal_components = pca.fit_transform(scaled_data)

# Determine the number of components to keep (e.g., explaining 95% of the variance)
explained_variance = np.cumsum(pca.explained_variance_ratio_)
n_components = np.argmax(explained_variance >= 0.95) + 1

# Create a new dataframe with the principal components
pca_data = pd.DataFrame(principal_components[:, :n_components], columns=[f'PC{i+1}' for i in range(n_components)])

# Add the target variable back to the PCA dataframe
pca_data['co2'] = reduced_data['co2'].values[:pca_data.shape[0]]

# Display the explained variance by the selected components
print(f"Selected {n_components} principal components explaining {explained_variance[n_components-1]*100:.2f}% of the variance.")

# Prepare the data for regression
X = pca_data.drop(columns=['co2'])
y = pca_data['co2']
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(y, X).fit()
print(model.summary())

# Plot residuals to check the model fit
residuals = model.resid
plt.figure(figsize=(10, 6))
sns.histplot(residuals, kde=True)
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

# Plot residuals vs. fitted values
fitted_values = model.fittedvalues
plt.figure(figsize=(10, 6))
plt.scatter(fitted_values, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title('Residuals vs. Fitted Values')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.show()
