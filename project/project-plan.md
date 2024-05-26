# Project Plan

## Title

Climate Change Analysis: Understanding the Relationship between Greenhouse Gas Emissions and Temperature Anomalies

## Main Question

1. What is the relationship between greenhouse gas emissions and temperature anomalies across different countries, and how does it vary based on regional, economic, and climatic factors?

## Description

Climate change is a pressing global issue with far-reaching implications for ecosystems, economies, and human well-being. This project aims to analyze the relationship between greenhouse gas emissions and temperature anomalies using data-driven methods. By examining emissions and temperature data from multiple countries, we seek to uncover patterns, trends, and potential causal relationships. Insights gained from this analysis can inform policy decisions, mitigation strategies, and adaptation measures to address climate change effectively.

In selecting countries for analysis, we considered several factors such as geographical diversity, economic significance, emissions intensity, and data availability. The chosen countries represent a range of regions, economic statuses, and emissions profiles, providing a comprehensive perspective on the global dynamics of climate change. Specifically, we have chosen:

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

This diverse set of countries provides a rich dataset for analyzing the complex interactions between emissions, temperature anomalies, and socio-economic factors.

## Datasources

### Datasource1: Annual Temperature Anomalies
* Metadata URL: N/A
* Data URL: https://ourworldindata.org/grapher/annual-temperature-anomalies
* Data Type: CSV

This dataset contains annual temperature anomaly data for various countries over a specified time period. Each record includes information such as the country, year, and temperature anomaly.

### Datasource2: Per Capita Greenhouse Gas Emissions
* Metadata URL: N/A
* Data URL: https://ourworldindata.org/explorers/co2?facet=none&country=DEU~USA~ZAF~RUS~CHN~JPN~IND~CAN~BRA~AUS&hideControls=false&Gas+or+Warming=All+GHGs+%28CO%E2%82%82eq%29&Accounting=Production-based&Fuel+or+Land+Use+Change=All+fossil+emissions&Count=Per+capita
* Data Type: CSV

This dataset provides per capita greenhouse gas emissions data for different countries over a specified time period. Each record includes information such as the country, year, and emissions in CO2 equivalents.

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

---

## 2. Dataset Content Mismatch

### Issue:
Upon retrieval of data from the GitHub repository for CO2 and greenhouse gas emissions, it became apparent that the dataset differed in format and content from the expected data, complicating data processing and analysis.

### Solution:
Thoroughly examined the dataset's documentation and structure to gain a better understanding of its contents and variables.

### Temporary Fix:
Filtered the dataset to include only the relevant columns (country, year, total_ghg) required for the project so that it's more in line with the format and content from the expected data and removed missing values from the total_ghg column to ensure data integrity.

---

## 3. Non-Consecutive Years in Dataset

### Issue:
The filtered dataset contained non-consecutive years, potentially affecting data continuity and analysis accuracy.

### Solution:
Considered implementing additional filtering criteria to include only consecutive years in the dataset, thereby enhancing data coherence and reliability.

### Temporary Fix:
Implemented a temporary fix to filter the dataset for consecutive years, albeit acknowledging the potential reduction in data size resulting from this approach.

---

## 4. Dependency on Annual Temperature Anomalies Dataset

### Issue:
The project's dependency on the Annual Temperature Anomalies dataset for aligning years and ensuring data consistency posed a significant challenge, especially in the absence of direct access to the dataset.

### Solution:
Explored various alternatives for aligning years across datasets, including integrating data from alternative sources or devising methods to estimate missing values.

### Temporary Fix:
Continued utilizing available datasets while developing strategies to handle missing or non-consecutive data points, prioritizing the maintenance of data integrity and project progress.


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
- Faced challenges in structuring the Datasource2 (Per Capita Greenhouse Gas Emissions) due to inconsistencies with the original data on ourworldindata.org.
- Investigated methods to filter and preprocess the data to align with project requirements.
- Explored potential modifications to the project question to accommodate alternative datasets or adjustments in data processing.
<!--
## Script Testing and Debugging
- Tested the data pipeline script locally to ensure its functionality.
- Identified and resolved issues related to data extraction, transformation, and storage.
- Collaborated with peers and mentors to troubleshoot challenging aspects of the script development.

## Project Plan Review
- Reviewed and updated the project plan to reflect changes in data availability and project scope.
- Documented challenges and considerations encountered during the data collection and preprocessing phases.
- Revisited the project objectives and refined the research question based on available datasets and project constraints.

## Script Deployment and Documentation
- Prepared the script (pipeline.py) for deployment by making it executable (pipeline.sh) and ensuring compatibility with GitHub workflows.
- Documented the script's functionality, input/output requirements, and potential troubleshooting steps.
- Updated the README.md file to provide instructions for running the script and accessing project resources.

## Final Review and Reflection
- Conducted a final review of the project components to ensure alignment with project objectives and requirements.
- Reflecting on the project journey, identified lessons learned and areas for improvement in future projects.
- Prepared for project presentation and discussion with mentors, incorporating feedback and insights gained throughout the project lifecycle.

## Project Conclusion
- Completed the data pipeline implementation, addressing challenges and adapting to changes in data availability and project scope.
- Compiled project documentation, including the project plan, script documentation, and project updates, for submission and review.
- Reflecting on the project experience, considered implications for future research and potential avenues for further exploration.
-->

