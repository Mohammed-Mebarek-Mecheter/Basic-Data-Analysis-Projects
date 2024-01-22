# Manga & Anime Dataset Analysis

## Overview

This project involves analyzing a [dataset](https://www.kaggle.com/datasets/duongtruongbinh/manga-and-anime-dataset) containing information on the top 10,000 manga and anime sourced from the popular website MyAnimeList. The dataset was crawled on January 6, 2024.

### Files
- `anime.csv`: Contains details on the top 10,000 anime entries.
- `manga.csv`: Contains details on the top 10,000 manga entries.

### Data Fields
Both datasets include various fields such as Title, Score, Vote, Ranked, Popularity, and more.

## Step 1: Data Exploration and Understanding

### 1.1 Load the Data
- Loaded `anime.csv` and `manga.csv` files into Python using Pandas.

### 1.2 Examine the Structure
- Checked the first few rows of each dataset to understand the structure.
- Explored data types, missing values, and general statistics.

### 1.3 Understand the Variables
- Reviewed the data fields in both datasets to understand the meaning of each variable.

### 1.4 Initial Summary
- Provided a brief summary of key statistics for important variables.

### 1.5 Explore Unique Values
- Identified unique values in categorical variables to understand the range of categories.

### 1.6 Data Cleaning
- Handled missing or inconsistent data.
- Replaced 'Unknown' values with NaN.
- Cleaned up 'Episodes', 'Duration', 'Members', 'Favorite', 'Volumes', 'Chapters'.
- Documented decisions and actions.

## Step 2: Preliminary Analysis

### 2.1 Top Rated Entries
- Identified the top-rated anime and manga based on user scores.

### 2.3 Popularity Insights
- Analyzed the relationship between popularity rank and user scores.

### 2.4 Source Material Influence
- Investigated the success of anime adaptations based on the source material.

## Step 3: Genre and Theme Analysis

### 3.1 Genre Distribution
- Explored the distribution of genres in manga.
- Cleaned up genre data by removing unwanted characters.

### 3.2 Common Themes
- Identified common themes explored in manga.

## Step 4: Production Insights

### 4.1 Studios and Producers
- Identified the top 10 most prolific animation studios.
- Identified the top 10 most prolific production companies.

### 4.3 Manga Serialization Impact
- Explored the impact of manga serialization platforms on manga success.

## Conclusion

This analysis provided insights into the world of manga and anime, exploring top-rated entries, popularity trends, source material impact, genre and theme distributions, and production insights. The cleaning and exploration processes were conducted to ensure meaningful and accurate analysis.
