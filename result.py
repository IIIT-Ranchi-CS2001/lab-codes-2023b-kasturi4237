import pandas as pd
import numpy as np

# Load the dataset
file_path = r'C:\Users\hp\Documents\pythonlabexam\AQI_Data.csv'
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Check the file path.")
    exit()

# Step 1: Display the first 8 columns
print("\nFirst 8 Columns:")
if data.shape[1] >= 8:
    first_8_columns = data.iloc[:, :8]
    print(first_8_columns)
else:
    print("Dataset has fewer than 8 columns.")

# Step 2: Display the last 5 rows
print("\nLast 5 Rows:")
print(data.tail(5))

# Step 3: Show the datatype and number of non-null values in each column
print("\nData Types and Non-Null Values:")
data_info = data.info()

# Step 4: Compute the mean AQI, max PM2.5, and min PM10 values for each city
# Ensure the necessary columns exist and are numeric
required_columns = ['City', 'AQI', 'PM2.5', 'PM10']
for col in required_columns:
    if col not in data.columns:
        print(f"Error: Column '{col}' not found in the dataset.")
        exit()

data['AQI'] = pd.to_numeric(data['AQI'], errors='coerce')
data['PM2.5'] = pd.to_numeric(data['PM2.5'], errors='coerce')
data['PM10'] = pd.to_numeric(data['PM10'], errors='coerce')

mean_aqi_per_city = data.groupby('City')['AQI'].mean()
max_pm25_per_city = data.groupby('City')['PM2.5'].max()
min_pm10_per_city = data.groupby('City')['PM10'].min()

print("\nMean AQI Per City:")
print(mean_aqi_per_city)

print("\nMax PM2.5 Per City:")
print(max_pm25_per_city)

print("\nMin PM10 Per City:")
print(min_pm10_per_city)

# Set-2, Question 2

# Step 1: Rename columns
data.rename(columns={
    'AQI': 'AIR QUALITY',
    'PM2.5': 'Particulate Matter 2.5',
    'PM10': 'Particulate Matter 10',
    'City': 'Location'
}, inplace=True)

# Step 2: Replace all occurrences of "Unknown" in the "Location" column with "not available"
if 'Location' in data.columns:
    data['Location'] = data['Location'].replace('Unknown', 'not available')

# Display the updated dataset (optional)
print("\nUpdated Dataset:")
print(data.head())

# Save the updated dataset to a new file (optional)
output_path = r'C:\Users\hp\Documents\pythonlabexam\AQI_Data_Updated.csv'
try:
    data.to_csv(output_path, index=False)
    print(f"\nUpdated dataset saved to: {output_path}")
except Exception as e:
    print(f"Error saving the file: {e}")
