import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import OLSInfluence, variance_inflation_factor

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

# # Standardize the data before applying PCA
# scaler = StandardScaler()
# scaled_data = scaler.fit_transform(reduced_numerical_data.dropna())

# # Apply PCA
# pca = PCA()
# principal_components = pca.fit_transform(scaled_data)

# # Determine the number of components to keep (e.g., explaining 95% of the variance)
# explained_variance = np.cumsum(pca.explained_variance_ratio_)
# n_components = np.argmax(explained_variance >= 0.95) + 1

# # Create a new dataframe with the principal components
# pca_data = pd.DataFrame(principal_components[:, :n_components], columns=[f'PC{i+1}' for i in range(n_components)])

# # Add the target variable back to the PCA dataframe
# pca_data['co2'] = reduced_data['co2'].values[:pca_data.shape[0]]

# # Display the explained variance by the selected components
# print(f"Selected {n_components} principal components explaining {explained_variance[n_components-1]*100:.2f}% of the variance.")

# # Prepare the data for regression
# X = pca_data.drop(columns=['co2'])
# y = pca_data['co2']
# X = sm.add_constant(X)

# # Fit the linear regression model
# model = sm.OLS(y, X).fit()
# print(model.summary())

# # Plot residuals to check the model fit
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

# # Step 1: Identify and Remove Outliers
# # Fit the linear regression model again to get influence measures
# model_influence = OLSInfluence(model)

# # Get studentized residuals
# studentized_residuals = model_influence.resid_studentized_external

# # Identify outliers (e.g., studentized residuals > 3 or < -3)
# outliers = np.where(np.abs(studentized_residuals) > 3)[0]

# # Remove outliers from the data
# pca_data_no_outliers = pca_data.drop(index=outliers)

# # Re-run the regression model without outliers
# X_no_outliers = pca_data_no_outliers.drop(columns=['co2'])
# y_no_outliers = pca_data_no_outliers['co2']
# X_no_outliers = sm.add_constant(X_no_outliers)

# model_no_outliers = sm.OLS(y_no_outliers, X_no_outliers).fit()
# print(model_no_outliers.summary())

# # Step 2: Transform the Dependent Variable
# # Apply log transformation to the dependent variable
# pca_data['log_co2'] = np.log1p(pca_data['co2'])  # log1p to handle zero values

# # Re-run the regression model with the transformed dependent variable
# X_log = pca_data.drop(columns=['co2', 'log_co2'])
# y_log = pca_data['log_co2']
# X_log = sm.add_constant(X_log)

# model_log = sm.OLS(y_log, X_log).fit()
# print(model_log.summary())

# # Plot residuals to check the model fit
# residuals_log = model_log.resid
# plt.figure(figsize=(10, 6))
# sns.histplot(residuals_log, kde=True)
# plt.title('Distribution of Residuals (Log Transformed)')
# plt.xlabel('Residuals')
# plt.ylabel('Frequency')
# plt.show()

# # Plot residuals vs. fitted values
# fitted_values_log = model_log.fittedvalues
# plt.figure(figsize=(10, 6))
# plt.scatter(fitted_values_log, residuals_log)
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Residuals vs. Fitted Values (Log Transformed)')
# plt.xlabel('Fitted Values')
# plt.ylabel('Residuals')
# plt.show()

# # Step 3: Explore Non-linear Relationships
# # Add polynomial terms to the principal components
# poly = PolynomialFeatures(degree=2, include_bias=False)
# poly_features = poly.fit_transform(pca_data.drop(columns=['co2', 'log_co2']))

# # Create a new dataframe with polynomial features
# poly_features_df = pd.DataFrame(poly_features, columns=poly.get_feature_names_out(pca_data.drop(columns=['co2', 'log_co2']).columns))

# # Add the dependent variable back
# poly_features_df['co2'] = pca_data['co2']

# # Re-run the regression model with polynomial features
# X_poly = poly_features_df.drop(columns=['co2'])
# y_poly = poly_features_df['co2']
# X_poly = sm.add_constant(X_poly)

# model_poly = sm.OLS(y_poly, X_poly).fit()
# print(model_poly.summary())

# # Plot residuals to check the model fit
# residuals_poly = model_poly.resid
# plt.figure(figsize=(10, 6))
# sns.histplot(residuals_poly, kde=True)
# plt.title('Distribution of Residuals (Polynomial Features)')
# plt.xlabel('Residuals')
# plt.ylabel('Frequency')
# plt.show()

# # Plot residuals vs. fitted values
# fitted_values_poly = model_poly.fittedvalues
# plt.figure(figsize=(10, 6))
# plt.scatter(fitted_values_poly, residuals_poly)
# plt.axhline(0, color='red', linestyle='--')
# plt.title('Residuals vs. Fitted Values (Polynomial Features)')
# plt.xlabel('Fitted Values')
# plt.ylabel('Residuals')
# plt.show()
