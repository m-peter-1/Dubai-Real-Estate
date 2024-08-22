# Dubai Real Estate Analysis and Predictions

## Overview

This project is based on a dataset for Dubai's real estate market, sourced from [Kaggle](https://www.kaggle.com/datasets/azharsaleem/real-estate-goldmine-dubai-uae-rental-market). The dataset offers a wealth of information about rental properties across various regions in Dubai. I conducted several case studies to extract actionable insights and demonstrate how even a seemingly simple dataset can provide significant business value when analyzed effectively.

## Packages and Tools Used

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib** & **Seaborn**: For data visualization.
- **Scikit-learn**: For machine learning models and evaluation.
- **Folium**: For interactive map visualizations.
- **GeoPandas**: For geographic data manipulation and plotting.

## Case Studies

### 1. Predicting Rental Prices

The first case study focuses on the classic machine learning problem of predicting rental prices in Dubai. After an exploratory data analysis (EDA) to understand the variables and assess data quality, I generated a predictive model. The key predictors identified included the size of the property in square feet and the number of bedrooms. These variables were used to build multiple models, including a simple linear regression model and a more complex machine learning algorithm. 

This case study answers key questions, such as: Can a more complex ML algorithm outperform a simpler model? How much better is the quality of predictions? In what areas do these models differ? The result is a predictive model that, using a few key variables, can accurately forecast potential rental income in Dubai's real estate market.

### 2. Identifying Optimal Property Types by Region

The second case study takes a more creative and visually-driven approach. Leveraging the geographical data in the dataset, I first cleaned and prepared the data, then performed clustering to divide Dubai into 20 distinct regions. In each region, I identified the property types that promise the highest revenue per square foot.

This analysis provides a visual decision-making tool for real estate developers, enabling them to pinpoint which property type—be it hotel apartments, villas, or residential buildings—yields the highest returns in each specific area of Dubai. The map created from this analysis reveals fascinating differences between regions and offers valuable insights for developers.
