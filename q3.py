try:
    # Determine the party with the highest number of seats in each state
    max_seats_per_state = df.loc[df.groupby("State")["Seats_Won"].idxmax()]

    # Display the state and the party with the highest number of seats
    print("\nParty with the highest number of seats in each state:")
    for _, row in max_seats_per_state.iterrows():
        print(f"{row['State']}: {row['Party']} ({row['Seats_Won']} seats)")
except KeyError:
    print("Error: Ensure the DataFrame contains the expected columns.")
except Exception as e:
    print(f"An unexpected error occurred while determining the highest seats: {e}")
