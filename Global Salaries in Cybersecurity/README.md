## Overview

This project involves the analysis of Global Salaries in Cybersecurity to gain insights into various factors influencing salaries. The [dataset](https://www.kaggle.com/datasets/infosecjobs/global-salaries-in-cybersecurity-infosec) contains information on work years, experience levels, employment types, job titles, salaries, and other relevant features.

## Steps Taken

### Step 1: Data Exploration

- Imported necessary libraries, including pandas, numpy, seaborn, and matplotlib.
- Loaded the dataset into a pandas DataFrame (`df_cleaned`).
- Conducted initial exploration using functions such as `info()`, `describe()`, and `head()` to understand the structure and contents of the dataset.

### Step 2: Data Cleaning

1. **Handling Missing Values:**
    - Checked for missing values (none found).

2. **Data Type Check:**
    - Checked and adjusted data types for each column as needed.

3. **Duplicate Check:**
    - Checked and removed duplicate rows (none found).
4. **Identifying Outliers:**
    - Used the interquartile range (IQR) method to identify and remove outliers.
    - Explored log transformation as an alternative approach to handling outliers.

### Step 3: Exploratory Data Analysis (EDA)

1. **Salary Distribution and Trends:**
    - Explored the overall distribution of salaries across work years and experience levels using box plots.
    - Analyzed how average salary changed for different employment types over time using point plots.

2. **Factors Influencing Salary:**
    - Explored average salaries by experience level, employment type, and company size using bar plots.
    - Visualized the salary distribution for top 10 job titles.

3. **Career Exploration and Insights:**

    - Explored the highest-paying job titles in the dataset.
    - Analyzed which countries offer the highest average salaries for specific job roles.

## Author

- Name: [Mohammed Mebarek Mecheter](https://www.linkedin.com/in/mohammed-mebarek-mecheter/)
- Email: mohammedmecheter@gmail.com

Feel free to contact me for any questions or additional information about this project.