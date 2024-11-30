import matplotlib.pyplot as plt
import numpy as np

# Data for the assembly elections
data = {
    "Madhya Pradesh": {"BJP": 163, "INC": 66, "BSP": 0, "Others": 1},
    "Rajasthan": {"BJP": 115, "INC": 69, "BSP": 2, "Others": 13},
}

# Function to calculate percentages
def calculate_percentage(seats):
    total_seats = sum(seats.values())
    return {party: (seats_won / total_seats) * 100 for party, seats_won in seats.items()}

# Calculate percentages for both states
mp_percentages = calculate_percentage(data["Madhya Pradesh"])
rj_percentages = calculate_percentage(data["Rajasthan"])

# Pie chart with the highest percentage slightly detached
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
for ax, (state, percentages) in zip(axes, {"Madhya Pradesh": mp_percentages, "Rajasthan": rj_percentages}.items()):
    wedges, texts, autotexts = ax.pie(
        percentages.values(),
        labels=percentages.keys(),
        autopct='%1.1f%%',
        explode=[0.1 if perc == max(percentages.values()) else 0 for perc in percentages.values()],
        startangle=90,
        shadow=True
    )
    ax.set_title(f"Party-wise Seat Share in {state}")

plt.tight_layout()
plt.show()

# Bar chart for both states
fig, ax = plt.subplots(figsize=(8, 6))
parties = list(data["Madhya Pradesh"].keys())
x = np.arange(len(parties))  # X positions for bars
bar_width = 0.35  # Width of bars

# Madhya Pradesh and Rajasthan seats
mp_seats = list(data["Madhya Pradesh"].values())
rj_seats = list(data["Rajasthan"].values())

# Plot the bars
ax.bar(x - bar_width / 2, mp_seats, width=bar_width, label="Madhya Pradesh")
ax.bar(x + bar_width / 2, rj_seats, width=bar_width, label="Rajasthan")

# Add labels, legend, and formatting
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.set_ylabel("Seats Won")
ax.set_title("Party-wise Seats Won in Assembly Elections 2023")
ax.legend(title="States")

plt.tight_layout()
plt.show()
