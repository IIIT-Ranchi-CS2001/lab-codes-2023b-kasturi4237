import pandas as pd
import numpy as np


file_path = 'C:\Users\hp\Documents\pythonlabexam\AQI_Data.csv' 
data = pd.read_csv(file_path)

# Step 1: Display the first 8 columns
print("First 8 Columns:")
first_8_columns = data.iloc[:, :8]
print(first_8_columns)

# Step 2: Display the last 5 rows
print("\nLast 5 Rows:")
last_5_rows = data.tail(5)
print(last_5_rows)

# Step 3: Show the datatype and number of non-null values in each column
print("\nData Types and Non-Null Values:")
data_info = data.info()

# Step 4: Compute the mean AQI, max PM2.5, and min PM10 values for each city
mean_aqi_per_city = data.groupby('City')['AQI'].mean()
max_pm25_per_city = data.groupby('City')['PM2.5'].max()
min_pm10_per_city = data.groupby('City')['PM10'].min()

# Display results
print("\nMean AQI Per City:")
print(mean_aqi_per_city)

print("\nMax PM2.5 Per City:")
print(max_pm25_per_city)

print("\nMin PM10 Per City:")
print(min_pm10_per_city)


#set-2
#question 2

# Step 1: Rename the column "AQI" to "AIR QUALITY"
data.rename(columns={'AQI': 'AIR QUALITY'}, inplace=True)

data.rename(columns={'PM2.5': 'Particulate Matter 2.5'}, inplace=True)

data.rename(columns={'PM10': 'Particulate matter 10'}, inplace=True)

data.rename(columns={'City': 'Location'}, inplace=True)

# Step 2: Replace all occurrences of "Unknown" in the "City" column with "not available"
data['City'] = data['City'].replace('Unknown', 'not available')

# Display the updated dataset (optional)
print("Updated Dataset:")
print(data.head())

