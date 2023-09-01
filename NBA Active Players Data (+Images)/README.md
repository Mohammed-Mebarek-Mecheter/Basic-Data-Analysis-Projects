# NBA Player Data Analysis Project

This is a data analysis project focused on NBA player attributes for the 2022-2023 season. The project involves data collection, data cleaning, data visualization, and the creation of an interactive data dashboard using Python libraries.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Getting Started](#getting-started)
- [Data Analysis and Visualization](#data-analysis-and-visualization)
- [Interactive Dashboard](#interactive-dashboard)
- [Contributing](#contributing)

## Project Overview

In this project, we aim to analyze and visualize various attributes of NBA players for the 2022-2023 season. The project includes the following key steps:

1. Data collection from the provided dataset.
2. Data cleaning and preprocessing.
3. Data analysis to answer specific questions.
4. Data visualization to present insights.
5. Creation of an interactive data dashboard using Dash.

## Dataset

The dataset used in this project contains information about NBA players active during the 2022-2023 season. The dataset includes player attributes such as name, position, height, weight, birthday, country of origin, school, and draft information.

- **Dataset File**: `players.csv` (CSV format)
- **Columns**: playerid, fname, lname, position, height, weight, birthday, country, school, draft_year, draft_round, draft_number

## Getting Started

To replicate or run this project on your local machine, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Mohammed-Mebarek-Mecheter/Basic-Data-Analysis-Projects.git
   cd NBA Active Players Data (+Images)
   ```

2. Install the required libraries:

   ```bash
   pip install dash dash-core-components dash-html-components pandas plotly
   ```

3. Run the Dash app:

   ```bash
   python app.py
   ```

   Open the local URL provided in your web browser to interact with the data dashboard.

## Data Analysis and Visualization

The project includes various data analysis tasks and visualizations to answer specific questions and present insights. Key analysis and visualizations include:

- [x] How many players are included in the dataset?
- [x] Are there any missing values in the dataset? If so, how are they handled?
- [x] What is the distribution of player positions in the dataset?
- [x] Which Top 10 countries are represented in the dataset, and how many players are from each country?
- [x] What are the unique schools from which players attended? Which schools are the most common?
- [x] What is the average height and weight of players in the dataset?
- [x] Is there a correlation between a player's height and weight?

## Interactive Dashboard

The project includes an interactive data dashboard created using Dash and Plotly. The dashboard combines multiple visualizations to provide an overview of player attributes, including scatter plots, histograms, and line charts.

To access the dashboard, run the Dash app as described in the "Getting Started" section and open the provided local URL in your web browser.

## Acknowledgments
The [dataset](https://www.kaggle.com/datasets/szymonjwiak/nba-active-players-data-images) was sourced from Kaggle.

## Contributing

Contributions to this project are welcome. If you have suggestions, improvements, or new features to add, please open an issue or submit a pull request.

Author: Mohammed Mebarek Mecheter