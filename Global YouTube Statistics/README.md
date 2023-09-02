# Global YouTube Statistics 2023

Welcome to the Global YouTube Statistics project! In this project, we explore a dataset containing statistics of the most subscribed YouTube channels. The goal is to gain valuable insights into the world of YouTube stardom and understand various factors contributing to channel success.

## Dataset Description

The dataset includes comprehensive details on top creators' subscriber counts, video views, upload frequency, country of origin, earnings, and more. It's a treasure trove of information for aspiring content creators, data enthusiasts, and those intrigued by the online content landscape.

## Key Features

The dataset includes the following key features:

- `rank`: The rank of the YouTuber in terms of subscribers.
- `Youtuber`: The name of the YouTuber.
- `subscribers`: The number of subscribers the YouTuber has.
- `video views`: The total number of views the YouTuber's videos have received.
- `category`: The category of the YouTuber's channel.
- `Title`: The title of the most recent video uploaded by the YouTuber.
- `uploads`: The number of videos uploaded by the YouTuber.
- `Country`: The country where the YouTuber is based.
- `Abbreviation`: The abbreviation of the country where the YouTuber is based.
- `channel_type`: The type of channel the YouTuber has (e.g., gaming, music, lifestyle).
- `video_views_rank`: The rank of the YouTuber in terms of video views.
- `country_rank`: The rank of the YouTuber in terms of subscribers from their country.
- `channel_type_rank`: The rank of the YouTuber in terms of subscribers from their channel type.
- `video_views_for_the_last_30_days`: The number of views the YouTuber's videos have received in the last 30 days.
- `lowest_monthly_earnings`: The lowest monthly earnings the YouTuber has made.
- `highest_monthly_earnings`: The highest monthly earnings the YouTuber has made.
- `lowest_yearly_earnings`: The lowest yearly earnings the YouTuber has made.
- `highest_yearly_earnings`: The highest yearly earnings the YouTuber has made.
- `subscribers_for_last_30_days`: The number of subscribers the YouTuber has gained in the last 30 days.
- `created_year`: The year the YouTuber's channel was created.
- `created_month`: The month the YouTuber's channel was created.
- `created_date`: The date the YouTuber's channel was created.
- `Gross tertiary education enrollment (%)`: The percentage of the population in the YouTuber's country that has completed some tertiary education.
- `Population`: The population of the YouTuber's country.
- `Unemployment rate`: The unemployment rate in the YouTuber's country.
- `Urban_population`: The percentage of the population in the YouTuber's country that lives in urban areas.
- `Latitude`: The latitude of the YouTuber's country.
- `Longitude`: The longitude of the YouTuber's country.


## Project Steps

1. **Project Setup**: Set up your development environment with the required Python libraries: NumPy, Pandas, Geopandas, Seaborn, and Matplotlib.

2. **Loading the Dataset**: Use Pandas to load the dataset (`"Global YouTube Statistics.csv"`) and get an overview of its structure using functions like `head()`, `info()`, and `describe()`.

3. **Descriptive Analysis**: Perform exploratory analysis to gain insights into the dataset. Visualize subscriber distribution, video views distribution, category distribution, upload frequency, top countries by channel count, etc.

4. **Identifying Trends Over Time**: Analyze trends over the last 15 years for metrics like subscribers gained, video views, and earnings. Create line plots to visualize these trends.

## Analyzing Trends Over Time

For the purpose of analyzing trends over time, we focused on the last 15 years of data. Here's a summary of the steps taken:

1. **Filtering Data**: We filtered the dataset to include only the last 15 years of data based on the 'created_year' column.

2. **Calculating Metrics**: We grouped the filtered data by 'created_year' and calculated metrics such as subscribers gained, video views, and earnings for each year.

3. **Creating Line Plots**: We used Seaborn and Matplotlib to create line plots to visualize the trends over time for subscribers gained, video views, and earnings.

## Project Setup

1. Clone this repository:

```bash
git clone https://github.com/Mohammed-Mebarek-Mecheter/Basic-Data-Analysis-Projects.git
cd Global YouTube Statistics
Install required libraries:
pip install pandas geopandas matplotlib seaborn
```
Run the Python scripts mentioned in the project steps to perform the data analysis and visualization.
interests or expand the project further.

## Acknowledgments
The [dataset](https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023) was sourced from Kaggle.

This project is for educational and research purposes.
Feel free to explore and modify the project to gain insights from the "Global YouTube Statistics 2023 Dataset."

Author: Mohammed Mebarek Mecheter
