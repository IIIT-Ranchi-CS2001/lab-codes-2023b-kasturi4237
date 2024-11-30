import os
import csv
import pandas as pd

# Data to be written to the file
election_data = [
    ["State", "Party", "Seats_Won", "Total_Seats", "Voter_Turnout (%)"],
    ["Madhya Pradesh", "BJP", 163, 230, 72.1],
    ["Madhya Pradesh", "INC", 66, 230, 72.1],
    ["Madhya Pradesh", "BSP", 0, 230, 72.1],
    ["Madhya Pradesh", "Others", 1, 230, 72.1],
    ["Rajasthan", "BJP", 115, 200, 74.2],
    ["Rajasthan", "INC", 69, 200, 74.2],
    ["Rajasthan", "BSP", 2, 200, 74.2],
    ["Rajasthan", "Others", 13, 200, 74.2],
]

file_name = "election_data.csv"

try:
    # Check if the file exists
    if not os.path.exists(file_name):
        # Create the file and write data
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(election_data)
        print(f"File '{file_name}' created and data written successfully.")
    else:
        print(f"File '{file_name}' already exists.")

    # Read the data into a Pandas DataFrame
    df = pd.read_csv(file_name)

    # Calculate the percentage of seats won by each party
    df['Seats_Percentage'] = (df['Seats_Won'] / df['Total_Seats']) * 100

    # Display the updated DataFrame
    print(df)

except PermissionError:
    print(f"Permission denied: Unable to create or write to '{file_name}'.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
