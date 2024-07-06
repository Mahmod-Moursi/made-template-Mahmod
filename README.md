# Exercise Badges

![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex1) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex2) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex3) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex4) ![](https://byob.yarr.is/Mahmod-Moursi/made-template-Mahmod/score_ex5)

# CO2 Emissions and Energy Consumption Analysis

## Description
This project analyzes CO2 emissions and energy consumption patterns across ten countries using statistical techniques and visualizations. The aim is to identify key factors affecting CO2 emissions, examine variations across countries, and offer actionable insights for policymakers to develop effective emission reduction strategies.

## Prerequisites
- Python 3.6 or higher
- Required libraries: pandas, numpy, matplotlib, seaborn, sklearn, statsmodels

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Mahmod-Moursi/your-repo-name.git
   cd your-repo-name
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



# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```

In this updated `README.md`, I've added sections relevant to my project while retaining the original template information. This ensures that all the necessary information is included and organized clearly.


