# Top 1000 Companies Data Analysis Project

This repository contains a data analysis project focused on the "Top 1000 Companies Dataset." The goal of this project is to explore, analyze, and visualize the characteristics of the top 1000 companies across various industries. The dataset includes information about company details, such as industry, growth percentage, location, and more.

## Dataset Information

- **Title:** Top 1000 Companies Dataset for Business Analysis
- **Description:** A comprehensive dataset containing details of the top 1000 fastest growing companies in the world.
- **Size:** 326KB
- **Format:** CSV (Comma-Separated Values)
- **Columns:** company_name, url, city, state, country, employees, linkedin_url, founded, Industry, GrowjoRanking, Previous Ranking, estimated_revenues, job_openings, keywords, LeadInvestors, Accelerator, btype, valuation, total_funding, product_url, indeed_url, growth_percentage, contact_info.

## Project Steps

1. **Load Dataset:** Used the pandas library to load the CSV dataset into a DataFrame.

2. **Check for Missing Values and Data Quality:** Investigated missing values, data types, and potential data quality issues. Explored columns with missing values, such as `url`, `state`, `linkedin_url`, etc.

3. **Identified Important Columns:** Identified relevant columns for analysis, such as `Industry`, `growth_percentage`, `city`, `state`, `country`, etc.

4. **Goals of the Project:** Defined goals for the data analysis project, such as analyzing industry distribution, growth patterns, geographic concentration, and more.

5. **Industry Distribution Analysis:** Analyzed the distribution of companies across different industries using bar plots. Visualized the distribution of the top 10 industries.

6. **Geographic Analysis:** Explored the representation of companies based on their location (city, state, country). Visualized the top 10 cities with the highest company concentration.

7. **Growth Analysis:** Investigated relationships between growth percentages and factors like previous ranking, valuation, and presence of lead investors or accelerators. Visualized these relationships using scatter plots and bar plots.

8. **Keywords Analysis:** Explored top keywords associated with the fastest-growing companies in different industries. Visualized the findings using word clouds.

9. **Lowest Growth Industries:** Identified the industries with the lowest average growth percentages and visualized them using bar plots.

## Project Setup

Clone this repository:

```bash
git clone https://github.com/Mohammed-Mebarek-Mecheter/Basic-Data-Analysis-Projects.git
cd Top 1000 Companies Details
Install required libraries:

pip install pandas matplotlib seaborn wordcloud

Run the Python scripts mentioned in the project steps to perform the data analysis and visualization.
```

## Acknowledgments
The dataset was sourced from [Kaggle](https://www.kaggle.com/datasets/amritpal24/top-1000-companies-details).

This project is for educational and research purposes.
Feel free to explore and modify the project to gain insights from the "Top 1000 Companies Dataset."

Author: Mohammed Mebarek Mecheter