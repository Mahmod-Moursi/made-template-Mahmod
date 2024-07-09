# Exercise Badges

![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex1) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex2) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex3) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex4) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex5)

# CO2 Emissions and Energy Consumption Analysis

## Description
This project aims to analyze the relationship between CO2 emissions and primary energy consumption across ten different countries. By using statistical techniques and visualizations, we seek to identify key factors affecting CO2 emissions, examine variations across countries, and offer actionable insights for policymakers to develop effective emission reduction strategies.

## Objectives
1.Analyze patterns in CO2 emissions and energy consumption: Understand the trends and correlations between these two critical variables.
2.Identify crucial factors impacting CO2 emissions: Determine what contributes most significantly to emissions.
3.Deliver actionable insights for policymakers: Provide recommendations based on our findings to help shape effective climate policies.

## Data Sources and Features
We merged data from two comprehensive datasets spanning from 2007 to 2016. Key features include:
-Year
-Country
-CO2 emissions
-Primary energy consumption
-GDP
-CO2 emissions from coal, oil, gas
-Population

## Data Preprocessing Steps
-Handling missing values: Ensuring data integrity by addressing null or empty entries.
-Normalization: Scaling data to ensure all variables have equal influence.
-Correlation analysis: Evaluating relationships between variables.
-VIF calculation: Identifying multicollinearity issues.
-PCA for dimensionality reduction: Reducing data dimensions while retaining key information.
-Outlier detection: Identifying and addressing anomalies in the data.

## Detailed Preprocessing Steps:
-Data Loading: Loaded data from CSV files using provided URLs and dropped columns with more than 50% missing values, as well as rows with any remaining missing values.
-Data Transformation: Identified common years across countries and filtered the data to include only valid countries and common years.
-Data Merging: Merged the CO2 and energy datasets on 'country', 'year', and 'iso_code' columns.
-Data Quality Assurance: Verified data consistency and accuracy.
-Data Analysis and Visualization: Analyzed the cleaned data and generated visualizations to gain insights and communicate findings.
-Output Destination: Saved the merged data to a CSV file named 'merged_data.csv'.
Note: While we focused on ten countries for this project, our process and code are designed to work with any set of countries. The merged dataset includes all countries shared by the original datasets, making our methodology flexible and widely applicable.

## Prerequisites
- Python 3.6 or higher
- Required libraries: pandas, numpy, matplotlib, seaborn, sklearn, statsmodels

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Mahmod-Moursi/made-template-Mahmod
   cd made-template-Mahmod
2. Install the required libraries:
   pip install -r requirements.txt

## Data
1. The data used for this analysis is included in the data/ directory:

merged_data.csv: Merged dataset containing CO2 emissions, primary energy consumption, GDP, and other relevant features.

## Running the Analysis
The analysis is divided into several scripts:
1. Exploratory Data Analysis:
	python scripts/eda.py
2. PCA and Regression Analysis:
	python scripts/pca_regression.py
3. Country-Specific Analysis:
	python scripts/country_analysis.py
4. Extended Analysis:
	python scripts/extended_analysis.py
	python scripts/extended_analysis2.py
	python scripts/extended_analysis3.py

## Report
The detailed analysis report is available in the analysis-report.pdf file.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
