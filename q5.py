import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    try:
        df = pd.read_csv(file_name)
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_name}' is empty.")
        df = pd.DataFrame()
    except pd.errors.ParserError:
        print(f"Error: Failed to parse the file '{file_name}'.")
        df = pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        df = pd.DataFrame()

    # Proceed only if the DataFrame is not empty
    if not df.empty:
        try:
            # Calculate the percentage of seats won by each party
            df['Seats_Percentage'] = (df['Seats_Won'] / df['Total_Seats']) * 100

            # Display the updated DataFrame
            print(df)

            # Create a bar chart showing the number of seats won by each party in each state
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x="State", y="Seats_Won", hue="Party")
            plt.title("Number of Seats Won by Each Party in Each State")
            plt.ylabel("Seats Won")
            plt.xlabel("State")
            plt.legend(title="Party")
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: Missing expected columns in the data: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero encountered while calculating percentages.")
        except Exception as e:
            print(f"An unexpected error occurred during calculations or plotting: {e}")
except PermissionError:
    print(f"Permission denied: Unable to create or write to '{file_name}'.")
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
