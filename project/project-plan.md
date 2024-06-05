# Project Plan

## Title

Climate Change Analysis: Understanding the Relationship between Greenhouse Gas Emissions and Energy Production

## Main Question

1. What is the relationship between greenhouse gas emissions and energy production across different countries, and how does it vary based on regional, economic, and climatic factors?

## Description

Climate change is a pressing global issue with far-reaching implications for ecosystems, economies, and human well-being. This project aims to analyze the relationship between greenhouse gas emissions and energy production using data-driven methods. By examining emissions and energy data from multiple countries, we seek to uncover patterns, trends, and potential causal relationships. Insights gained from this analysis can inform policy decisions, mitigation strategies, and adaptation measures to address climate change effectively.

In selecting countries for detailed analysis, we considered factors such as geographical diversity, economic significance, emissions intensity, and data availability. The chosen countries represent a range of regions, economic statuses, and emissions profiles, providing a comprehensive perspective on the global dynamics of climate change. Specifically, we have chosen:

- United States: Major emitter, highly industrialized.
- China: World's largest emitter, significant economic influence.
- India: Rapidly growing economy, populous nation.
- Brazil: Rich biodiversity, deforestation concerns.
- Germany: Leading in renewable energy adoption.
- Russia: Major fossil fuel producer.
- Japan: Highly industrialized, advanced technology.
- South Africa: Developing country with coal reliance.
- Australia: Reliant on fossil fuels, vulnerable to climate impacts.
- Canada: Abundant natural resources, emissions from oil extraction.

This diverse set of countries provides a rich dataset for analyzing the complex interactions between emissions, energy production, and socio-economic factors.

## Datasources

### Datasource1: CO2 and Greenhouse Gas Emissions
* Metadata URL: [CO2 Data Metadata](https://github.com/owid/co2-data/blob/master/owid-co2-data.csv)
* Data URL: [CO2 Data](https://github.com/owid/co2-data)
* Data Type: CSV

This dataset contains data on CO2 and greenhouse gas emissions for various countries over a specified time period. Each record includes information such as the country, year, population, GDP, total greenhouse gas emissions, and per capita emissions.

### Datasource2: Energy
* Metadata URL: [Energy Data Metadata](https://github.com/owid/energy-data/blob/master/owid-energy-data.csv)
* Data URL: [Energy Data](https://github.com/owid/energy-data)
* Data Type: CSV

This dataset provides data on energy production and consumption for different countries over a specified time period. Each record includes information such as the country, year, population, GDP, total electricity generation, and emissions from electricity generation.

## Work Packages

1. **Data Acquisition and Preprocessing** [#1][i1]
   - Obtain and preprocess temperature anomalies and greenhouse gas emissions datasets.
   - Ensure data consistency, handle missing values, and standardize country names.

2. **Country Selection and Filtering** [#2][i2]
   - Select a subset of countries for analysis based on relevance and data availability.
   - Filter datasets to include only selected countries and common years.

3. **Correlation Analysis** [#3][i3]
   - Explore the correlation between greenhouse gas emissions and temperature anomalies.
   - Investigate how the correlation varies across different countries and regions.

[i1]: https://github.com/Mahmod-Moursi/made-template-Mahmod/issues/1
[i2]: https://github.com/Mahmod-Moursi/made-template-Mahmod/issues/2
[i3]: https://github.com/Mahmod-Moursi/made-template-Mahmod/issues/3

# Project Issue Log

## 1. Difficulty in Locating Dataset

### Issue:
Finding the direct link to download the Annual Temperature Anomalies dataset from Our World in Data proved challenging, hindering progress in accessing necessary project data.

### Solution:
Contacted Our World in Data for assistance in locating the dataset and explored alternative sources to obtain the required data.

### Temporary Fix:
As a temporary measure, utilized the available GitHub repository for the CO2 and greenhouse gas emissions dataset from Our World in Data as a substitute for the missing temperature anomalies dataset.

### Resolution:
Ultimately decided to replace the Annual Temperature Anomalies dataset with a more relevant and accessible dataset from Our World in Data, focusing on energy production.

---

## 2. Dataset Content Mismatch

### Issue:
Upon retrieval of data from the GitHub repository for CO2 and greenhouse gas emissions, it became apparent that the dataset differed in format and content from the data on the Our World in Data website, complicating data processing and analysis.

### Solution:
Thoroughly examined the dataset's documentation and structure to gain a better understanding of its contents and variables.

### Resolution:
Decided to rely solely on the data from the GitHub repository, ensuring consistency and simplifying data processing.

---

## 3. Non-Consecutive Years in Dataset

### Issue:
The filtered dataset contained non-consecutive years, potentially affecting data continuity and analysis accuracy.

### Solution:
Considered implementing additional filtering criteria to include only consecutive years in the dataset, thereby enhancing data coherence and reliability.

### Update:
Revised the data processing script to ensure that both the CO2 and Greenhouse Gas Emissions dataset and the Energy dataset include only consecutive years for each country, maintaining consistency and reliability in the analysis.

---

## 4. Dependency on Annual Temperature Anomalies Dataset

### Issue:
The project's dependency on the Annual Temperature Anomalies dataset for aligning years and ensuring data consistency posed a significant challenge, especially in the absence of direct access to the dataset.

### Solution:
Explored various alternatives for aligning years across datasets, including integrating data from alternative sources or devising methods to estimate missing values.

### Resolution:
Revised the project plan to replace the Annual Temperature Anomalies dataset with an energy production dataset, ensuring the project's continuity and relevance to the revised research question.

# Project Updates

## Project Initiation
- Started the project by reviewing the project requirements and objectives outlined in the project plan.
- Identified the key tasks and milestones necessary to complete the project successfully.

## Data Collection
- Researched and identified potential data sources relevant to the project's objectives.
- Found and selected the primary dataset (Datasource1: CO2 and Greenhouse Gas Emissions) from ourworldindata.org.
- Encountered difficulties in acquiring the data from Datasource2: Annual Temperature Anomalies.
- Explored alternative datasets and considered how they could complement the primary dataset.

## Script Development
- Began developing the data pipeline script (pipeline.py) to automate the data collection and transformation process.
- Made scripts executable using chmod +x command to ensure they can be run as entry points for the data pipeline.
- Committed changes to Git and pushed them to the GitHub repository for review and collaboration.
- Tested the data pipeline script locally to verify its functionality and ensure it saves the processed data in the appropriate directory.
- Faced challenges in structuring the Datasource2 (Per Capita Greenhouse Gas Emissions) due to inconsistencies with the original data on ourworldindata.org.
- Investigated methods to filter and preprocess the data to align with project requirements.
- Explored potential modifications to the project question to accommodate alternative datasets or adjustments in data processing.

## Data Refinement and Analysis Preparation
- Updated the project question to focus on the relationship between greenhouse gas emissions and energy production.
- Refined the selection of columns from both datasets to streamline data analysis while retaining essential information.
- Finalized the script to filter and merge the datasets, ensuring data consistency and completeness.

## Next Steps
- Perform trend analysis on greenhouse gas emissions and energy production.
- Explore relationships between energy sources and greenhouse gas emissions.
- Investigate the impact of economic and regional factors on emissions and energy consumption.
